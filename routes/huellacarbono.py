import json
from click import Choice
from fastapi import APIRouter
from models.huellacarbono import HuellaCarbono, HuellaCarbonoCrear
from config.db import SessionDep
from config import config
from config.config import settings
from functools import lru_cache
import google.generativeai as genai

@lru_cache
def get_settings():
    return config.Settings()

API_KEY=settings.API_KEY
genai.configure(api_key=API_KEY)

huellacarbono = APIRouter()

@huellacarbono.post("/calcular-co2", response_model=HuellaCarbono)
async def calcular_huella_carbono(huellaCarbono: HuellaCarbonoCrear, session: SessionDep):
    """
    Calcula la huella de carbono a partir de los valores ingresados.
    """
    kilometros_recorridos = huellaCarbono.kilometros_recorridos
    indice_eficiencia = huellaCarbono.indice_eficiencia
    tipo_combustible = huellaCarbono.tipo_combustible

    carbon_footprint = kilometros_recorridos * indice_eficiencia

    # Usar el modelo generativo para obtener el resultado
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"""
    Analiza los datos ingresados y proporciona un párrafo con los hallazgos o conclusiones, adicional haz una lista de vehiculos con mejores alternativas. todo en formato markdown.

    Kilómetros recorridos: {kilometros_recorridos} 
    Índice de eficiencia: {indice_eficiencia} 
    Huella de carbono generada: {carbon_footprint} gramos de CO2 generados

    Para que lo tengas en cuenta, el calculo de la huella de barcono se genera a partir de los kilometros recorridos y la eficiencia del vehiculo, se hace mendiante una multiplicación y el resultado es la cantidad de CO2 que se emite al ambiente en krilogramos.
    """

    response = model.generate_content(prompt)
    hallazgos = response.text

    huella_carbono = HuellaCarbono(
        kilometros_recorridos=kilometros_recorridos,
        indice_eficiencia=indice_eficiencia,
        tipo_combustible=tipo_combustible,
        huella_carbono=carbon_footprint,
        hallazgos=hallazgos
    )

    session.add(huella_carbono)
    session.commit()
    session.refresh(huella_carbono)

    return huella_carbono


@huellacarbono.get("/calcular-co2/{id}", response_model=HuellaCarbono)
async def obtener_huella_carbono( id: int, session: SessionDep):
    """
    Obetener la huella de carbono por su ID.
    """
    huellaCarbono = session.query(HuellaCarbono).filter(HuellaCarbono.huella_carbono_id == id).first()
    if huellaCarbono is None:
        return {"error": "Huella de carbono not found"}
    return huellaCarbono

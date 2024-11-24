from fastapi import APIRouter
from models.huellacarbono import HuellaCarbono, HuellaCarbonoCrear
from config.db import SessionDep

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

    huellaCarbono = HuellaCarbono(
        kilometros_recorridos=kilometros_recorridos,
        indice_eficiencia=indice_eficiencia,
        tipo_combustible=tipo_combustible,
        huella_carbono=carbon_footprint
    )
    
    session.add(huellaCarbono)
    session.commit()
    session.refresh(huellaCarbono)

    return huellaCarbono


@huellacarbono.get("/calcular-co2/{id}", response_model=HuellaCarbono)
async def obtener_huella_carbono( id: int, session: SessionDep):
    """
    Obetener la huella de carbono por su ID.
    """
    huellaCarbono = session.query(HuellaCarbono).filter(HuellaCarbono.huella_carbono_id == id).first()
    if huellaCarbono is None:
        return {"error": "Huella de carbono not found"}
    return huellaCarbono

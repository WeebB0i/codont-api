from fastapi import APIRouter
from models.huellacarbono import HuellaCarbono, HuellaCarbonoCrear
from config.db import SessionDep

huellacarbono = APIRouter()

@huellacarbono.post("/calcular-co2", response_model=HuellaCarbono)
async def calculate_carbon_footprint(huellaCarbono: HuellaCarbonoCrear, session: SessionDep):
    kilometros_recorridos = huellaCarbono.kilometros_recorridos
    indice_eficiencia = huellaCarbono.indice_eficiencia
    tipo_combustible = huellaCarbono.tipo_combustible

    # Example calculation (values are illustrative)
    if tipo_combustible == "gasolina":
        emission_factor = 2.31  # kg CO2 per liter
    elif tipo_combustible == "diesel":
        emission_factor = 2.68  # kg CO2 per liter
    else:
        return {"error": "Unsupported fuel type"}

    fuel_consumed = kilometros_recorridos / indice_eficiencia
    carbon_footprint = fuel_consumed * emission_factor

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
async def get_carbon_footprint( id: int, session: SessionDep):
    huellaCarbono = session.query(HuellaCarbono).filter(HuellaCarbono.huella_carbono_id == id).first()
    if huellaCarbono is None:
        return {"error": "Huella de carbono not found"}
    return huellaCarbono

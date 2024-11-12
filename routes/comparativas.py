# myapi/routers/vehiculos.py
from fastapi import APIRouter, HTTPException
from models.comparativas import Comparativa, ComparativaResponse
from sqlmodel import select
from typing import List
from config.db import SessionDep
from models.vehiculo import Vehiculo

# Crear el router de FastAPI para vehículos
comparativas = APIRouter()

@comparativas.get("/comparativas/", response_model=List[ComparativaResponse])
def listar_comparativas(session: SessionDep):
    """
    Listar todas las comparativas de vehículos.
    """
    comparativas = session.exec(select(Comparativa)).all()
    lista_comparativas = []
    
    for comparativa in comparativas:
        vehiculo_id_1 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == comparativa.vehiculo_id_1)).first()
        vehiculo_id_2 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == comparativa.vehiculo_id_2)).first()
        
        
        comparacion_resultado = ComparativaResponse(
            comparativa_id=comparativa.comparativa_id,
            vehiculo_id_1={
                "id": vehiculo_id_1.vehiculo_id,
                "marca": vehiculo_id_1.marca,
                "modelo": vehiculo_id_1.modelo,
                "anio": vehiculo_id_1.anio,
                "eficiencia": vehiculo_id_1.eficiencia,
                "tipo_combustible": vehiculo_id_1.tipo_combustible,
                "capacidad_carga": vehiculo_id_1.capacidad_carga, 
                "tipo_vehiculo": vehiculo_id_1.tipo_vehiculo,
                "consumo_combustible": vehiculo_id_1.consumo_combustible,
            },
            vehiculo_id_2={
                "id": vehiculo_id_2.vehiculo_id,
                "marca": vehiculo_id_2.marca,
                "modelo": vehiculo_id_2.modelo,
                "anio": vehiculo_id_2.anio,
                "eficiencia": vehiculo_id_2.eficiencia,
                "tipo_combustible": vehiculo_id_2.tipo_combustible,
                "capacidad_carga": vehiculo_id_2.capacidad_carga, 
                "tipo_vehiculo": vehiculo_id_2.tipo_vehiculo, 
                "consumo_combustible": vehiculo_id_1.consumo_combustible,

            }
        )
        
        lista_comparativas.append(comparacion_resultado)
    
    return lista_comparativas

@comparativas.post("/comparativas/", response_model=Comparativa)
def crear_comparativa(
    vehiculo_id_1: int, vehiculo_id_2: int, session: SessionDep,
):
    """
    Crear una nueva comparativa entre dos vehículos.
    """
    # Verificar que ambos vehículos existan
    vehiculo_1 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == vehiculo_id_1)).first()
    vehiculo_2 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == vehiculo_id_2)).first()

    if not vehiculo_1 or not vehiculo_2:
        raise HTTPException(status_code=404, detail="Uno o ambos vehículos no fueron encontrados.")

    # Crear y almacenar la nueva comparativa
    comparativa = Comparativa(vehiculo_id_1=vehiculo_id_1, vehiculo_id_2=vehiculo_id_2)
    session.add(comparativa)
    session.commit()
    session.refresh(comparativa)

    return comparativa
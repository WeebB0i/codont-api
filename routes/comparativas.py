# myapi/routers/vehiculos.py
from fastapi import APIRouter, Depends, HTTPException, Query
from models.comparativas import Comparativa
from sqlmodel import Session, select
from typing import Annotated, List
from config.db import crear_vehiculos, create_db_and_tables, SessionDep, get_session
from models.usuario import Usuario
from models.vehiculo import Vehiculo, VehiculoCrear

# Crear el router de FastAPI para vehículos
comparativas = APIRouter()

@comparativas.on_event("startup")
def on_startup():
    create_db_and_tables([Usuario.__table__, Vehiculo.__table__, Comparativa.__table__])
    
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
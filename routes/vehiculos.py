from fastapi import APIRouter, Query
from sqlmodel import select
from typing import Annotated, List
from config.db import SessionDep
from models.usuario import Usuario
from models.vehiculo import Vehiculo, VehiculoCrear

# Crear el router de FastAPI para vehículos
vehiculos = APIRouter()

# Crear un endpoint para obtener todos los vehículos
@vehiculos.get("/vehiculos/", response_model=List[Vehiculo])
def get_vehiculos(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100, 
    ):
    """
    Obtener todos los vehículos registrados.
    """
    vehiculos = session.exec(select(Vehiculo).offset(offset).limit(limit)).all()
    return vehiculos

# Endpoint para crear un nuevo vehículo
@vehiculos.post("/vehiculos/", response_model=VehiculoCrear)
def create_vehiculo(vehiculo: VehiculoCrear, session: SessionDep):
    """
    Crear un nuevo vehículo.
    """
    # Agregar el nuevo vehículo a la sesión y confirmarlo
    db_vehiculo = Vehiculo.from_orm(vehiculo);
    session.add(db_vehiculo)
    session.commit()
    session.refresh(db_vehiculo)
    return db_vehiculo

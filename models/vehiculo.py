# models/vehiculo.py
from sqlmodel import SQLModel, Field
from typing import Optional

class VehiculoBase(SQLModel):
    tipo_vehiculo: str = Field(max_length=30)
    eficiencia: int 
    marca: str = Field(max_length=50)
    modelo: str = Field(max_length=50)
    anio: int
    consumo_combustible: float
    capacidad_carga: int
    tipo_combustible: str = Field(max_length=50)

class Vehiculo(VehiculoBase, table=True):
    __tablename__ = "vehiculo"
    vehiculo_id: Optional[int] = Field(default=None, primary_key=True)

class VehiculoCrear(VehiculoBase):
    class Config:
        orm_mode = True
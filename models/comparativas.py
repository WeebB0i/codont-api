# models/vehiculo.py
from models.vehiculo import Vehiculo
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class ComparativaBase(SQLModel):
    vehiculo_1: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_1]"})
    vehiculo_2: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_2]"})

class Comparativa(SQLModel, table=True):
    __tablename__ = "comparativa"
    comparativa_id: Optional[int] = Field(default=None, primary_key=True)
    # Relaciones con los modelos de vehículos
    vehiculo_1: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_1]"})
    vehiculo_2: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_2]"})

class ComparativaResponse(ComparativaBase):
    vehiculo_1: dict
    vehiculo_2: dict
    eficiencia_diferencia: float
    class Config:
        orm_mode = True
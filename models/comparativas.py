# models/comparativa.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from models.vehiculo import Vehiculo

class ComparativaBase(SQLModel):
    vehiculo_id_1: Optional[int] = Field(default=None, foreign_key="vehiculo.vehiculo_id")
    vehiculo_id_2: Optional[int] = Field(default=None, foreign_key="vehiculo.vehiculo_id")

class Comparativa(ComparativaBase, table=True):
    __tablename__ = "comparativa"
    comparativa_id: Optional[int] = Field(default=None, primary_key=True)
    # Relaciones con los modelos de vehículos
    vehiculo_1: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_1]"})
    vehiculo_2: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_2]"})

class ComparativaResponse(ComparativaBase):
    comparativa_id: int
    vehiculo_id_1: dict
    vehiculo_id_2: dict
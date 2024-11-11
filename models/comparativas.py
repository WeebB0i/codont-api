# models/vehiculo.py
from models.vehiculo import Vehiculo
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Comparativa(SQLModel, table=True):
    _tablename_ = "comparativa"
    comparativa_id: Optional[int] = Field(default=None, primary_key=True)
    vehiculo_id_1: int = Field(foreign_key="vehiculo.vehiculo_id")
    vehiculo_id_2: int = Field(foreign_key="vehiculo.vehiculo_id")
    
    # Relaciones con los modelos de vehículos
    vehiculo_1: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_1]"})
    vehiculo_2: Optional[Vehiculo] = Relationship(sa_relationship_kwargs={"foreign_keys": "[Comparativa.vehiculo_id_2]"})
# myapi/models/usuario.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    
    usuario_id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50)
    email: str = Field(max_length=100)

    # Relaciones
    # vehiculos: List["Vehiculo"] = Relationship(back_populates="usuario")
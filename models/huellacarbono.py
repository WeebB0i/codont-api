from sqlmodel import SQLModel, Field
from typing import Optional

class HuellaCarbonoBase(SQLModel):
    kilometros_recorridos: float
    indice_eficiencia: float
    tipo_combustible: str

class HuellaCarbono(HuellaCarbonoBase, table=True):
    __tablename__ = "huella_carbono"
    huella_carbono_id: int = Field(default=None, primary_key=True)
    huella_carbono: Optional[float] = None
    hallazgos: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class HuellaCarbonoCrear(HuellaCarbonoBase):
    class Config:
        from_attributes = True
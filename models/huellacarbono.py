from sqlmodel import Field, SQLModel


class HuellaCarbonoBase(SQLModel):
    kilometros_recorridos: float
    indice_eficiencia: float
    tipo_combustible: str

class HuellaCarbono(HuellaCarbonoBase, table=True):
    __tablename__ = "huella_carbono"
    huella_carbono_id: int = Field(default=None, primary_key=True)

class HuellaCarbonoCrear(HuellaCarbonoBase):
    class Config:
        orm_mode = True
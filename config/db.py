from typing import Annotated

from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends

from models.vehiculo import Vehiculo


sqlite_file_name = "basededatos.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables(tables_order):
    SQLModel.metadata.create_all(engine, tables=tables_order)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def crear_vehiculos():
    with Session(engine) as session:
        for vehiculo_data in vehiculos_data:
            vehiculo = Vehiculo(**vehiculo_data)
            session.add(vehiculo)
        session.commit()

vehiculos_data = [
    {
        "tipo_vehiculo": "Moto",
        "eficiencia": 60,
        "marca": "Boxer",
        "modelo": "CT 100",
        "anio": 2022,
        "consumo_combustible": 1.8
    },
    {
        "tipo_vehiculo": "Moto",
        "eficiencia": 60,
        "marca": "AKT",
        "modelo": "NKD 125",
        "anio": 2020,
        "consumo_combustible": 2.5
    },
    {
        "tipo_vehiculo": "Moto",
        "eficiencia": 90,
        "marca": "Honda",
        "modelo": "CBF 125",
        "anio": 2023,
        "consumo_combustible": 1.5
    },
    {
        "tipo_vehiculo": "Furgoneta",
        "eficiencia": 207,
        "marca": "Peugeot",
        "modelo": "Boxer",
        "anio": 2018,
        "consumo_combustible": 6.7
    },
    {
        "tipo_vehiculo": "Furgoneta",
        "eficiencia": 207,
        "marca": "Renault",
        "modelo": "Kangoo",
        "anio": 2022,
        "consumo_combustible": 6.3
    },
    {
        "tipo_vehiculo": "Furgoneta",
        "eficiencia": 221,
        "marca": "Nissan",
        "modelo": "NV350",
        "anio": 2019,
        "consumo_combustible": 9.25
    },
    {
        "tipo_vehiculo": "Furgón",
        "eficiencia": 161,
        "marca": "Chevrolet",
        "modelo": "NHR Reward",
        "anio": 2023,
        "consumo_combustible": 16.9
    },
    {
        "tipo_vehiculo": "Furgón",
        "eficiencia": 161,
        "marca": "Foton",
        "modelo": "Aumark S3",
        "anio": 2022,
        "consumo_combustible": 13.4
    },
    {
        "tipo_vehiculo": "Furgón",
        "eficiencia": 250,
        "marca": "Hino",
        "modelo": "Dutro Pro Serie 300",
        "anio": 2022,
        "consumo_combustible": 12.5
    }
]

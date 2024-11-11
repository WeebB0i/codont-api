# myapi/routers/vehiculos.py
from fastapi import APIRouter, Depends, HTTPException, Query
from models.comparativas import Comparativa, ComparativaResponse
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

@comparativas.get("/comparativas/", response_model=List[ComparativaResponse])
def listar_comparativas(session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100, ):
    """
    Listar todas las comparativas de vehículos.
    """
    # comparativas = session.exec(select(Comparativa)).all()
    # lista_comparativas = []
    
    # for comparativa in comparativas:
    #     vehiculo_1 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == comparativa.vehiculo_id_1)).first()
    #     vehiculo_2 = session.exec(select(Vehiculo).where(Vehiculo.vehiculo_id == comparativa.vehiculo_id_2)).first()
        
        
        # comparacion_resultado = ComparativaResponse(
        #     comparativa_id=comparativa.comparativa_id,
        #     vehiculo_1={
        #         "marca": vehiculo_1.marca,
        #         "modelo": vehiculo_1.modelo,
        #         "anio": vehiculo_1.anio,
        #         "eficiencia": vehiculo_1.eficiencia,
        #     },
        #     vehiculo_2={
        #         "marca": vehiculo_2.marca,
        #         "modelo": vehiculo_2.modelo,
        #         "anio": vehiculo_2.anio,
        #         "eficiencia": vehiculo_2.eficiencia,
        #     }
        # )
        
        # lista_comparativas.append(comparacion_resultado)
    
    # return lista_comparativas

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
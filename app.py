from config.db import create_db_and_tables, crear_vehiculos
from models.comparativas import Comparativa
from models.usuario import Usuario
from models.vehiculo import Vehiculo
from routes.comparativas import comparativas
from fastapi import FastAPI
# from pyngrok import ngrok
from routes.vehiculos import vehiculos

# Inicia el túnel Ngrok
# public_url = ngrok.connect(8000)
# print(f"Tu API está disponible en: {public_url}")

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables([Usuario.__table__, Vehiculo.__table__, Comparativa.__table__])
    crear_vehiculos()
    
app.include_router(vehiculos)
app.include_router(comparativas)


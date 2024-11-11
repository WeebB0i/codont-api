import uvicorn
from fastapi import FastAPI
# from pyngrok import ngrok
from routes.vehiculos import vehiculos

# Inicia el túnel Ngrok
# public_url = ngrok.connect(8000)
# print(f"Tu API está disponible en: {public_url}")

app = FastAPI()

app.include_router(vehiculos)


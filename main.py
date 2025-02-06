import os
from fastapi import FastAPI
import uvicorn
from db import create_all_tables, SessionDeep
from sqlmodel import select
from models import BaseSchema
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env
#Routes
from routes import wishes, users

app = FastAPI(
    lifespan=create_all_tables,    #se ejecuta al principio y al final de la app
)

app.include_router(wishes.route)
app.include_router(users.route)

# Recuperar valores de las variables de entorno
allow_origins = os.getenv("CORS_ALLOW_ORIGINS").split(",")
allow_methods = os.getenv("CORS_ALLOW_METHODS").split(",")
# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # Permite todas las solicitudes de todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get('/')
def root(session: SessionDeep):
    return {'Hello': 'World'}



if __name__ == '__main__':
  port = int(os.environ.get("PORT", 8000))
  uvicorn.run("main:app", host="0.0.0.0", port=port)
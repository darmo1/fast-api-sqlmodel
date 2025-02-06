from fastapi import FastAPI
from db import create_all_tables, SessionDeep
from sqlmodel import select
from models import BaseSchema
from fastapi.middleware.cors import CORSMiddleware

#Routes
from routes import wishes, users

app = FastAPI(
    lifespan=create_all_tables,    #se ejecuta al principio y al final de la app
)

app.include_router(wishes.route)
app.include_router(users.route)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

@app.get('/')
def root(session: SessionDeep):
    return {'Hello': 'World'}
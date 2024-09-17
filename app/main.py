from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import video_endpoint
from app.helpers.database_helper import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(video_endpoint.router)



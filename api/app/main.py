from fastapi import FastAPI

from .database import Base, engine
from .routers import productos, categorias


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Tienda Virtual",
    description="API del Taller 3 - Lenguaje de Programación",
    version="1.0.0"
)


app.include_router(productos.router)
app.include_router(categorias.router)


@app.get("/")
def root():
    return {
        "mensaje": "API de Tienda Virtual funcionando"
    }

from pydantic import BaseModel, ConfigDict


class CategoriaBase(BaseModel):
    id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


class ProductoBase(BaseModel):
    id: int
    sku: str
    marca: str
    nombre: str
    precio: float
    foto: str | None = None
    stock: int
    activo: bool
    disponible: bool
    categoria: CategoriaBase

    model_config = ConfigDict(from_attributes=True)
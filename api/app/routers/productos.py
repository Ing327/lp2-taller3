from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get(
    "/",
    response_model=list[schemas.ProductoBase]
)
def listar_productos(
    categoria_id: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_productos(
        db,
        categoria_id
    )


@router.get(
    "/{sku}",
    response_model=schemas.ProductoBase
)
def obtener_producto(
    sku: str,
    db: Session = Depends(get_db)
):
    producto = crud.get_producto_by_sku(
        db,
        sku
    )

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto
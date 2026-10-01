from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db


router = APIRouter(
    prefix="/categorias",
    tags=["Categorías"]
)


@router.get(
    "/",
    response_model=list[schemas.CategoriaBase]
)
def listar_categorias(
    db: Session = Depends(get_db)
):
    return crud.get_categorias(db)
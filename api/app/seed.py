import json
import os

from sqlalchemy.orm import Session

from .database import Base, SessionLocal, engine
from .models import Categoria, Producto


Base.metadata.create_all(bind=engine)


def cargar_productos():
    ruta = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "productos.json"
    )

    with open(ruta, "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    db: Session = SessionLocal()

    try:
        for datos in productos:
            nombre_categoria = datos.get("categoria")

            if not nombre_categoria:
                nombre_categoria = "General"

            categoria = (
                db.query(Categoria)
                .filter(Categoria.nombre == nombre_categoria)
                .first()
            )

            if categoria is None:
                categoria = Categoria(
                    nombre=nombre_categoria
                )
                db.add(categoria)
                db.flush()

            producto_existente = (
                db.query(Producto)
                .filter(Producto.sku == datos["sku"])
                .first()
            )

            if producto_existente is not None:
                continue

            producto = Producto(
                sku=datos["sku"],
                marca=datos["marca"],
                nombre=datos["nombre"],
                precio=datos["precio"],
                foto=datos.get("foto"),
                stock=datos.get("stock", 0),
                activo=datos.get("activo", True),
                categoria_id=categoria.id
            )

            db.add(producto)

        db.commit()

        print("Datos cargados correctamente.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    cargar_productos()
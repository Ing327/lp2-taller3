from flask import Blueprint, render_template, request

from . import api_client


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    categoria = request.args.get("categoria", "").strip()

    if categoria:
        try:
            categoria_id = int(categoria)
        except ValueError:
            categoria_id = None
    else:
        categoria_id = None

    productos = api_client.obtener_productos(categoria_id)
    categorias = api_client.obtener_categorias()

    return render_template(
        "index.html",
        productos=productos,
        categorias=categorias,
        categoria_seleccionada=categoria_id
    )


@bp.route("/producto/<sku>")
def detalle(sku):
    producto = api_client.obtener_producto(sku)

    if producto is None:
        return render_template(
            "404.html"
        ), 404

    return render_template(
        "detalle.html",
        producto=producto
    )


@bp.route("/categorias")
def categorias():
    categorias = api_client.obtener_categorias()

    return render_template(
        "categorias.html",
        categorias=categorias
    )


@bp.route("/buscar")
def buscar():
    sku = request.args.get("sku", "").strip()

    if not sku:
        return render_template(
            "404.html"
        ), 404

    producto = api_client.obtener_producto(sku)

    if producto is None:
        return render_template(
            "404.html"
        ), 404

    return render_template(
        "detalle.html",
        producto=producto
    )
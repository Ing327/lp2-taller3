import requests

from config import API_URL


def obtener_productos(categoria_id=None):
    try:
        params = {}

        if categoria_id is not None:
            params["categoria_id"] = categoria_id

        respuesta = requests.get(
            f"{API_URL}/productos/",
            params=params,
            timeout=5
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException:
        return []


def obtener_producto(sku):
    try:
        respuesta = requests.get(
            f"{API_URL}/productos/{sku}",
            timeout=5
        )

        if respuesta.status_code == 404:
            return None

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException:
        return None


def obtener_categorias():
    try:
        respuesta = requests.get(
            f"{API_URL}/categorias/",
            timeout=5
        )

        respuesta.raise_for_status()

        return respuesta.json()

    except requests.RequestException:
        return []
# Taller 3 - Tienda Virtual

# AUTOR

GUSTAVO ADOLFO VALENCIA AGUDELO

## Descripción

Este proyecto corresponde al **Taller 3** de Lenguajes de Programación.

La aplicación implementa una tienda virtual utilizando una arquitectura compuesta por tres servicios principales:

- **Web:** aplicación frontend desarrollada con Flask.
- **API:** backend desarrollado con FastAPI.
- **Base de datos:** PostgreSQL.
- **Docker Compose:** utilizado para ejecutar y comunicar los diferentes servicios.

La aplicación permite consultar un catálogo de productos, visualizar el detalle de cada producto, realizar búsquedas mediante SKU y filtrar los productos por categoría.

---

## Tecnologías utilizadas

- Python
- Flask
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- HTML
- CSS
- Jinja2
- JSON

---

## Estructura del proyecto

```text
lp2-taller3/
│
├── docker-compose.yml
├── .env
├── .env.example
├── README.md
│
├── docs/
│   └── GUIA.md
│
├── web/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── config.py
│   ├── run.py
│   │
│   └── app/
│       ├── __init__.py
│       ├── routes.py
│       ├── api_client.py
│       │
│       ├── static/
│       │   ├── css/
│       │   │   └── style.css
│       │   └── images/
│       │
│       └── templates/
│           ├── base.html
│           ├── index.html
│           ├── detalle.html
│           ├── categorias.html
│           └── 404.html
│
└── api/
    ├── Dockerfile
    ├── requirements.txt
    │
    ├── data/
    │   └── productos.json
    │
    └── app/
        ├── __init__.py
        ├── main.py
        ├── database.py
        ├── models.py
        ├── schemas.py
        ├── crud.py
        ├── seed.py
        │
        └── routers/
            ├── __init__.py
            ├── productos.py
            └── categorias.py
```

---

# Arquitectura del proyecto

El proyecto utiliza tres servicios independientes:

```text
                    ┌──────────────────────┐
                    │      Navegador        │
                    │   localhost:5000      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       WEB            │
                    │       Flask          │
                    │      Puerto 5000     │
                    └──────────┬───────────┘
                               │
                               │ HTTP
                               ▼
                    ┌──────────────────────┐
                    │        API           │
                    │       FastAPI        │
                    │      Puerto 8000     │
                    └──────────┬───────────┘
                               │
                               │ SQLAlchemy
                               ▼
                    ┌──────────────────────┐
                    │      DATABASE        │
                    │      PostgreSQL      │
                    │      Puerto 5432     │
                    └──────────────────────┘
```

### Funcionamiento

1. El usuario accede a la aplicación mediante el navegador.
2. Flask muestra las páginas HTML.
3. Flask realiza solicitudes HTTP a FastAPI.
4. FastAPI consulta PostgreSQL.
5. PostgreSQL devuelve la información.
6. FastAPI entrega los datos a Flask.
7. Flask muestra los productos en el navegador.

---

# Configuración de variables de entorno

El archivo `.env` contiene:

```env
POSTGRES_USER=tienda_user
POSTGRES_PASSWORD=cambia_esta_clave
POSTGRES_DB=tienda_db
SECRET_KEY=cambia-esta-clave-tambien
```

Para comenzar desde el archivo de ejemplo:

```bash
cp .env.example .env
```

El archivo `.env` contiene información de configuración y no debe publicarse en repositorios públicos.

---

# Base de datos

La base de datos utilizada es PostgreSQL.

Las tablas principales son:

```text
categorias
│
├── id
└── nombre


productos
│
├── id
├── sku
├── marca
├── nombre
├── precio
├── foto
├── stock
├── activo
└── categoria_id
```

Existe una relación entre ambas tablas:

```text
CATEGORIA
    │
    │ 1
    │
    │ N
    ▼
PRODUCTO
```

Una categoría puede tener varios productos y cada producto pertenece a una categoría.

---

# Modelo Producto

Los productos manejan los siguientes datos:

| Campo | Descripción |
|---|---|
| `id` | Identificador del producto |
| `sku` | Código único del producto |
| `marca` | Marca del producto |
| `nombre` | Nombre del producto |
| `precio` | Precio del producto |
| `foto` | Imagen del producto |
| `stock` | Cantidad disponible |
| `activo` | Indica si el producto está activo |
| `categoria_id` | Categoría a la que pertenece |

También existe la propiedad `disponible`, que permite determinar si el producto está disponible utilizando su estado y cantidad de stock.

---

# Datos de productos

Los productos se encuentran en:

```text
api/data/productos.json
```

Ejemplo:

```json
{
    "sku": "AUD-001",
    "marca": "Sony",
    "nombre": "Audífonos WH-1000XM4",
    "precio": 1199000,
    "foto": "images/audifonos-sony.jpg",
    "stock": 0,
    "activo": true,
    "categoria": "Audio"
}
```

Las categorías utilizadas actualmente son:

- Audio
- Computación
- Gaming
- Celulares

---

# Carga de datos

Los datos de `productos.json` son cargados a PostgreSQL mediante:

```text
api/app/seed.py
```

Para ejecutar la carga:

```bash
docker compose exec api python -m app.seed
```

Cuando la carga se realiza correctamente aparece:

```text
Datos cargados correctamente.
```

El proceso:

1. Lee `productos.json`.
2. Obtiene la categoría del producto.
3. Crea la categoría si no existe.
4. Comprueba si el SKU ya existe.
5. Crea el producto.
6. Guarda los datos en PostgreSQL.

También se cargan los valores de `stock` y `activo`.

---

# Ejecución del proyecto

## 1. Entrar en la carpeta

```bash
cd lp2-taller3
```

## 2. Configurar `.env`

```bash
cp .env.example .env
```

Verificar:

```env
POSTGRES_USER=tienda_user
POSTGRES_PASSWORD=cambia_esta_clave
POSTGRES_DB=tienda_db
SECRET_KEY=cambia-esta-clave-tambien
```

## 3. Construir los contenedores

```bash
docker compose build
```

## 4. Iniciar los servicios

```bash
docker compose up -d
```

Comprobar el estado:

```bash
docker compose ps
```

## 5. Cargar los productos

```bash
docker compose exec api python -m app.seed
```

---

# Acceso a la aplicación

Aplicación web:

```text
http://localhost:5000
```

API:

```text
http://localhost:8000
```

Documentación automática de FastAPI:

```text
http://localhost:8000/docs
```

---

# Funcionalidades

## Catálogo de productos

Ruta:

```text
/
```

La página principal muestra el catálogo de productos obtenido desde la API.

---

## Buscar producto por SKU

Ruta:

```text
/buscar?sku=SKU
```

Ejemplo:

```text
http://localhost:5000/buscar?sku=COM-001
```

Si el SKU existe, se muestra el detalle del producto.

Si el SKU no existe, se muestra la página de producto no encontrado.

---

## Detalle de producto

Ruta:

```text
/producto/<sku>
```

Ejemplo:

```text
http://localhost:5000/producto/COM-001
```

Si el SKU no existe, se devuelve un error HTTP 404.

---

## Categorías

Ruta:

```text
/categorias
```

Ejemplo:

```text
http://localhost:5000/categorias
```

También es posible filtrar productos por categoría desde el catálogo.

---

# API

El backend está desarrollado utilizando FastAPI.

## Productos

Obtener productos:

```http
GET /productos/
```

Obtener producto mediante SKU:

```http
GET /productos/{sku}
```

Filtrar productos por categoría:

```http
GET /productos/?categoria_id=1
```

## Categorías

Obtener categorías:

```http
GET /categorias/
```

---

# Cliente de API

Flask utiliza:

```text
web/app/api_client.py
```

Funciones principales:

```python
obtener_productos()
obtener_producto(sku)
obtener_categorias()
```

La comunicación sigue el flujo:

```text
Flask → FastAPI → PostgreSQL
```

Flask no consulta directamente PostgreSQL.

---

# Rutas de Flask

```text
/
```

Página principal.

```text
/producto/<sku>
```

Detalle de producto.

```text
/categorias
```

Listado de categorías.

```text
/buscar
```

Búsqueda mediante SKU.

---

# Manejo de errores

Cuando un producto no existe se utiliza:

```text
404 Not Found
```

La plantilla utilizada es:

```text
web/app/templates/404.html
```

---

# Docker Compose

Los servicios están definidos en:

```text
docker-compose.yml
```

Servicios:

```text
database
api
web
```

### Database

PostgreSQL 15.

Puerto:

```text
5432
```

### API

FastAPI.

Puerto:

```text
8000
```

### Web

Flask.

Puerto:

```text
5000
```

---

# Comandos útiles

Ver contenedores:

```bash
docker compose ps
```

Logs del servicio web:

```bash
docker compose logs --tail=50 web
```

Logs de la API:

```bash
docker compose logs --tail=50 api
```

Logs de PostgreSQL:

```bash
docker compose logs --tail=50 database
```

Reiniciar web:

```bash
docker compose restart web
```

Reiniciar todos:

```bash
docker compose restart
```

Detener servicios:

```bash
docker compose down
```

Detener servicios y eliminar datos de PostgreSQL:

```bash
docker compose down -v
```

---

# Reiniciar completamente la base de datos

Si se necesita comenzar nuevamente con los datos de `productos.json`:

```bash
docker compose down -v
docker compose up -d --build
docker compose exec api python -m app.seed
docker compose restart web
```

> `docker compose down -v` elimina el volumen de PostgreSQL y los datos almacenados en esa base de datos.

---

# Gestión del stock

Cada producto tiene un campo `stock` en:

```text
api/data/productos.json
```

Ejemplo:

```json
"stock": 8
```

El archivo `seed.py` utiliza el valor:

```python
stock=datos.get("stock", 0)
```

También utiliza:

```python
activo=datos.get("activo", True)
```

Si los productos ya existían en PostgreSQL antes de realizar un cambio en el proceso de carga, puede ser necesario reconstruir la base de datos:

```bash
docker compose down -v
docker compose up -d --build
docker compose exec api python -m app.seed
```

---

# Imágenes

Las imágenes deben estar ubicadas en:

```text
web/app/static/images/
```

Los nombres definidos en `productos.json` deben coincidir con los archivos existentes.

Ejemplo:

```text
web/app/static/images/
├── audifonos-sony.jpg
├── parlante-jbl.jpg
├── galaxy-buds.jpg
├── mx-master-3s.jpg
├── teclado-k380.jpg
├── monitor-hp-24.jpg
├── razer-deathadder.jpg
├── hyperx-alloy.jpg
└── galaxy-a55.jpg
```

---

# Git

Comprobar cambios:

```bash
git status
```

Agregar cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Taller 3 tienda virtual"
```

Enviar a GitHub:

```bash
git push
```

> No se recomienda subir `.env` al repositorio cuando contiene contraseñas o claves privadas.

---

# Solución de problemas

## Página en blanco

Revisar los logs:

```bash
docker compose logs --tail=50 web
```

También:

```bash
docker compose logs --tail=50 api
```

Verificar que `base.html` tenga la estructura HTML y los bloques utilizados por las demás plantillas.

---

## Los productos aparecen con stock 0

Verificar que `productos.json` tenga:

```json
"stock": 8
```

y que `seed.py` utilice:

```python
stock=datos.get("stock", 0)
```

Si los productos ya existían en PostgreSQL, reconstruir la base:

```bash
docker compose down -v
docker compose up -d --build
docker compose exec api python -m app.seed
```

---

## No aparece una categoría

Verificar el campo:

```json
"categoria": "Nombre de categoría"
```

en:

```text
api/data/productos.json
```

---

## Error 404 al buscar un SKU

Verificar que el SKU exista en:

```text
api/data/productos.json
```

Ejemplo:

```text
COM-001
```

La búsqueda se realiza mediante:

```text
/buscar?sku=COM-001
```

---

# Conclusión

El Taller 3 implementa una tienda virtual utilizando una arquitectura de múltiples servicios.

El proyecto integra:

- Flask para la interfaz web.
- FastAPI para la API.
- PostgreSQL para almacenar la información.
- SQLAlchemy para trabajar con la base de datos.
- Docker Compose para ejecutar los servicios.
- JSON para proporcionar los datos iniciales.
- Jinja2 para generar las páginas HTML.

La aplicación permite consultar productos, buscar productos mediante SKU, visualizar detalles, consultar categorías y filtrar productos por categoría.


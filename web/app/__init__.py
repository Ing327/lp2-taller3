
from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object(config_class)

    # Registrar las rutas
    from .routes import bp

    app.register_blueprint(bp)

    return app
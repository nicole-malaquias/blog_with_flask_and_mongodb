# Arquivo: app/__init__.py

from flask import Flask
# Importando as rotas
from app import views


def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    # Camada de Views desacoplada
    views.init_app(app)

    return app
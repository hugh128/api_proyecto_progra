from flask import Flask
from routes.warsharll_routes import warshall_bp

def create_app():
    app = Flask(__name__)

    # Agregar rutas
    app.register_blueprint(warshall_bp)

    return app
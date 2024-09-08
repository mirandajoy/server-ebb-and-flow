from flask import Flask
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    CORS(app)

    from .routes.images import images_bp
    app.register_blueprint(images_bp)

    @app.get("/")
    def index():
        return "Ebb & Flow API"
    
    return app
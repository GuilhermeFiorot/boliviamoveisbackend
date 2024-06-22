from flask import Flask
from .core.config import Config
from .core.database import db, migrate
from .api import api_blueprint
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    JWTManager(app)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
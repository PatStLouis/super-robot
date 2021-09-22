from flask import Flask, session
from config import Config
import json


def init_app(app_config=Config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    with app.app_context():
        from .main import bp as main_bp

        app.register_blueprint(main_bp)

        return app
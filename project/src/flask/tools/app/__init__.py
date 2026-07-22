from flask import Flask
from .config import Config
import os


def create_app():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    app.config.from_object(Config)

    from app.routes import bp

    app.register_blueprint(bp)

    return app
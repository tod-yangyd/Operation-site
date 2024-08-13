from flask import Flask
from config import configs


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    print(app.config)
    configs[config_name].init_app(app)

    from .base import base as base_blueprint
    app.register_blueprint(base_blueprint)

    return app


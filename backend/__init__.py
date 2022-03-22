from flask import Flask
from flask_restx import Api
from config import config

from .aadhaar_verifier_api_namespace import aadhaar_verifier_api_ns


api = Api(
    version="1.0",
    title="Aadhaar Verifier Flask APIs",
    description="Aadhaar Verifier Flask APIs",
)
api.add_namespace(aadhaar_verifier_api_ns)


def create_app(config_name):

    app = Flask(__name__)
    config_class = config[config_name]
    config_object = config_class(app)
    app.config.from_object(config_object)
    config_object.init_app()
    config_object.print_items()

    return app

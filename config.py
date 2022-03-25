import os
import logging
from tabulate import tabulate
from werkzeug.middleware.proxy_fix import ProxyFix

from core.utils import LogFilter
from core.constants import LOG_RECORD_FORMAT, LOG_DATETIME_FORMAT


BASE_DIR = os.path.dirname(__file__)


class Config:
    # Default configurations for all environments
    FLASK_APP = os.getenv(key="FLASK_APP", default="aadhaar_verifier.py")
    PORT = os.getenv(key="PORT", default=9000)
    LOGGER_NAME = "aadhaar_verifier_logger"
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "backend/upload_folder/")

    def __init__(self, app):
        self.app = app

    def init_app(self):
        # Logger Configuration
        self.app.logger = logging.getLogger(self.LOGGER_NAME)
        self.app.logger.propagate = False
        log_filter = LogFilter()
        self.app.logger.addFilter(log_filter)

        # Log Handler Configuration
        std_err_handler = logging.StreamHandler()
        log_formatter = logging.Formatter(
            fmt=LOG_RECORD_FORMAT, datefmt=LOG_DATETIME_FORMAT
        )
        std_err_handler.setFormatter(log_formatter)
        self.app.logger.addHandler(std_err_handler)

        # WSGI Configuration
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

    def print_items(self):
        print(
            tabulate(
                tabular_data=[
                    ["FLASK_APP", self.FLASK_APP],
                    ["PORT", self.PORT],
                    ["LOGGER_NAME", self.LOGGER_NAME],
                    ["UPLOAD_FOLDER", self.UPLOAD_FOLDER],
                ],
                headers=("VARIABLE", "VALUE"),
            )
        )


class LocalConfig(Config):
    ENV = "localhost"
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG

    def init_app(self):
        super().init_app()
        self.app.logger.setLevel(self.LOGGING_LEVEL)


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    LOGGING_LEVEL = logging.DEBUG

    def init_app(self):
        super().init_app()
        self.app.logger.setLevel(self.LOGGING_LEVEL)


class DockerConfig(Config):
    ENV = "docker"
    DEBUG = True
    LOGGING_LEVEL = logging.INFO

    def init_app(self):
        super().init_app()
        self.app.logger.setLevel(self.LOGGING_LEVEL)


class TestingConfig(Config):
    ENV = "testing"
    DEBUG = False
    LOGGING_LEVEL = logging.INFO

    def init_app(self):
        super().init_app()
        self.app.logger.setLevel(self.LOGGING_LEVEL)


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    LOGGING_LEVEL = logging.ERROR

    def init_app(self):
        super().init_app()
        self.app.logger.setLevel(self.LOGGING_LEVEL)


config = {
    "local": LocalConfig,
    "development": DevelopmentConfig,
    "docker": DockerConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

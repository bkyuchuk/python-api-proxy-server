"""The app module, containing the app factory function."""
from flask import Flask
from flask_cors import CORS

from exceptions import WeatherException
from routes import blueprint
from settings import Config

cors = CORS()


def create_app(config_object=Config):
    """
    An application factory method, as explained here:
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/

    Parameters:
    config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_errorhandlers(app)
    register_blueprints(app)
    return app


def register_errorhandlers(app: Flask) -> None:
    def errorhandler(error: WeatherException):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(WeatherException)(errorhandler)


def register_blueprints(app: Flask) -> None:
    """
    Register Flask blueprints and enable CORS.
    """
    origins = app.config.get("CORS_ORIGIN_WHITELIST", "*")
    cors.init_app(blueprint, origins=origins)
    app.register_blueprint(blueprint)

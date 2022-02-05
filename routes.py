import requests
from flask import Blueprint, request

from exceptions import WeatherException
from settings import Config

blueprint = Blueprint("weather", __name__)


@blueprint.route("/api", methods=("GET",))
def get_weather():
    city = request.args.get("q")
    payload = {"q": city, Config.API_KEY_NAME: Config.API_KEY_VALUE}
    response = requests.get(Config.API_BASE_URL, params=payload)

    if response.status_code == 404:
        raise WeatherException.city_not_found()

    if response.status_code == 401:
        raise WeatherException.unauthorized()

    return response.json()

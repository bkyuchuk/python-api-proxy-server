from flask import Blueprint, current_app, request
from requests import RequestException
from requests import get as http_get

from config import DevConfig
from exceptions import WeatherException

blueprint = Blueprint("weather", __name__)


@blueprint.route("/api", methods=("GET",))
def get_weather():
    """
    Get the weather for a given city passed as a URL param.
    """
    payload = {
        DevConfig.API_KEY_NAME: DevConfig.API_KEY_VALUE,
        **request.args,
    }

    try:
        response = http_get(DevConfig.API_BASE_URL, params=payload)

        if response.status_code != 200:
            raise get_weather_exception(response.status_code)
        else:
            return response.json()

    except RequestException as e:
        current_app.logger.exception("A network problem occured.", e)


def get_weather_exception(status_code: int) -> WeatherException:
    possible_exceptions = {
        404: WeatherException.city_not_found(),
        401: WeatherException.unauthorized(),
        429: WeatherException.limit_exceeded(),
    }
    return possible_exceptions.get(status_code, WeatherException.unknown())

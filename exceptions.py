from flask import jsonify


def create_exception(data: list[str], code=500):
    """
    Create a dict containing the `text` and `code` of the
    exception to be created.
    """
    return {"message": {"errors": {"body": data}}, "status_code": code}


CITY_NOT_FOUND = create_exception(["City not found."], code=404)
UNAUTHORIZED = create_exception(["Invalid API key."], code=401)
UNKNOWN = create_exception(["Unknown error."], code=500)


class WeatherException(Exception):
    status_code = 500

    def __init__(
        self,
        message,
        payload: str = None,
        status_code: int = None,
    ) -> None:
        Exception.__init__(self)
        self.message = message
        self.payload = payload
        self.status_code = status_code

    def to_json(self):
        return jsonify(self.message)

    @classmethod
    def city_not_found(cls):
        return cls(**CITY_NOT_FOUND)

    @classmethod
    def unauthorized(cls):
        return cls(**UNAUTHORIZED)

    @classmethod
    def unknown(cls):
        return cls(**UNKNOWN)

import pytest
from flask import Flask, url_for
from webtest import TestApp

from app import create_app
from config import TestConfig
from exceptions import CITY_NOT_FOUND

"""
General test setup. Pytest's fixtures need to be in this file,
because they get injected in the test class.
"""


@pytest.fixture(scope="function")
def test_app(app: Flask) -> TestApp:
    """A Webtest app."""
    return TestApp(app)


@pytest.fixture(scope="function")
def app():
    """An application for the tests."""
    _app = create_app(config_object=TestConfig)

    context = _app.test_request_context()
    context.push()

    yield _app

    context.pop()


class TestRoutes:
    def test_get_weather_ok(self, test_app: TestApp):
        res = test_app.get(url_for("weather.get_weather", q="Seattle"))
        assert res.json["name"] == "Seattle"
        assert res.status_int == 200

    def test_get_weather_not_found(self, test_app: TestApp):
        res = test_app.get(
            url_for("weather.get_weather", q="SeattleTralala"),
            expect_errors=True,
        )
        assert res.json == CITY_NOT_FOUND["message"]
        assert res.status_int == 404

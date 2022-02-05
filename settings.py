import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base configuration."""

    API_BASE_URL = os.environ.get("API_BASE_URL", "base-url")
    API_KEY_NAME = os.environ.get("API_KEY_NAME", "api-key-name")
    API_KEY_VALUE = os.environ.get("API_KEY_VALUE", "api-key-value")
    CORS_ORIGIN_WHITELIST = [
        # TODO: Change before deployment
        "http://127.0.0.1:5500",
        "http://0.0.0.0:5500",
    ]

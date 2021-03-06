import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base configuration."""

    API_BASE_URL = os.environ.get("API_BASE_URL", "base-url")
    API_KEY_NAME = os.environ.get("API_KEY_NAME", "api-key-name")
    API_KEY_VALUE = os.environ.get("API_KEY_VALUE", "api-key-value")


class ProdConfig(Config):
    """Prod configuration"""

    ENV = "prod"
    DEBUG = False


class DevConfig(Config):
    """Dev configuration"""

    ENV = "dev"
    DEBUG = True


class TestConfig(Config):
    """Test configuration"""

    TESTING = True
    DEBUG = True

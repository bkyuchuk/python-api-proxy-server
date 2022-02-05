from app import create_app
from config import DevConfig, ProdConfig


def test_prod_config():
    """Prod config."""
    app = create_app(config_object=ProdConfig)
    assert app.config["ENV"] == "prod"
    assert not app.config["DEBUG"]


def test_dev_config():
    """Dev config."""
    app = create_app(config_object=DevConfig)
    assert app.config["ENV"] == "dev"
    assert app.config["DEBUG"]

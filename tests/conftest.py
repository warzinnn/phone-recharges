import pytest

import src.infrastructure.entities.orm as orm
from src.infrastructure.web_flask.app import create_app


@pytest.fixture(scope="session")
def app():
    """Fixtures for API Testing"""
    app = create_app()
    app.config.from_object("src.infrastructure.web_flask.config.DevelopmentConfig")
    print(f"[+] Testing: {app.config['TESTING']}")
    yield app


@pytest.fixture(scope="session")
def set_mappers():
    orm.configure_mappers()

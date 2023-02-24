import src.infrastructure.entities.orm as ORM
import pytest
from app import create_app


"""Fixtures for API Testing"""
@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config.from_object("config.TestingConfig")
    print(f"[+] Testing: {app.config['TESTING']}")
    yield app

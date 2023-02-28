import pytest

from app import create_app


@pytest.fixture(scope="session")
def app():
    """Fixtures for API Testing"""
    app = create_app()
    app.config.from_object("config.TestingConfig")
    print(f"[+] Testing: {app.config['TESTING']}")
    yield app

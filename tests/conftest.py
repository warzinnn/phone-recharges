import pytest

from app import create_app


from src.infrastructure.config.connection import DBConnectionHandler
from src.domain.model.products import Products
from src.domain.model.company import Company
from src.domain.model.recharge import Recharge


@pytest.fixture(scope="session")
def app():
    """Fixtures for API Testing"""
    app = create_app()
    app.config.from_object("config.TestingConfig")
    print(f"[+] Testing: {app.config['TESTING']}")
    yield app

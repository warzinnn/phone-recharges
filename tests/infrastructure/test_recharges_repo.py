
from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from mock_alchemy.mocking import AlchemyMagicMock
from src.domain.model.recharge import Recharge
from src.domain.model.products import Products
from src.infrastructure.repository.recharges_repository import RechargeRepository

class ConnectionHandlerMock:
    """
    STUB Data
    """

    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Recharge),
                        mock.call.join(Products, Products.id == Recharge.product_id),
                        mock.call.with_entities
                    ],
                    [(Recharge("5511999999999", "fake_product_01"), 50.0, 'claro_11')]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

@pytest.fixture
def configure_repo():
    """Fixture to return the ProductsRepository with the mock connection"""
    return RechargeRepository(ConnectionHandlerMock)



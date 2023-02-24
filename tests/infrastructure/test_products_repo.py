from unittest import mock

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.domain.products import Products
from src.infrastructure.repository.products_repository import \
    ProductsRepository


class ConnectionHandlerMock:
    """
    STUB Data
    """

    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Products)],
                    [Products("fake-product_20", 20.0, "fake_company_20")],
                ),
                (
                    [
                        mock.call.query(Products),
                        mock.call.filter(Products.id == "fake-product_15"),
                    ],
                    [Products("fake-product_15", 15.0, "fake_company_11")],
                ),
                (
                    [
                        mock.call.query(Products),
                        mock.call.filter(Products.value == 35.0),
                    ],
                    [Products("fake-product_35", 35.0, "fake_company_11")],
                ),
                (
                    [
                        mock.call.query(Products),
                        mock.call.filter(Products.id_company == "fake_company_21"),
                    ],
                    [Products("fake-product_05", 5.0, "fake_company_21")],
                ),
                (
                    [
                        mock.call.query(Products),
                        mock.call.filter(Products.id == "mock_50"),
                    ],
                    [],  # Empty list to enter in the condition of product id not in database
                ),
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


@pytest.fixture
def configure_repo():
    """Fixture to return the ProductsRepository with the mock connection"""
    return ProductsRepository(ConnectionHandlerMock)


class TestProductsRepository:
    def test_select_all_products(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_products()
        assert isinstance(data[0], Products)
        assert data[0].id == "fake-product_20"
        assert data[0].value == 20.0

    def test_select_product_by_id(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_id("fake-product_15")
        assert isinstance(data[0], Products)
        assert data[0].id == "fake-product_15"
        assert data[0].value == 15.0

    def test_select_product_by_value(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'value'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_value(35.0)
        assert isinstance(data[0], Products)
        assert data[0].id == "fake-product_35"
        assert data[0].value == 35.0

    def test_select_products_by_company(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id_company'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_products_by_company("fake_company_21")
        assert isinstance(data[0], Products)
        assert data[0].id == "fake-product_05"
        assert data[0].value == 5.0
        assert data[0].id_company == "fake_company_21"

    def test_create_new_product(self, configure_repo):
        """
        GIVEN a product is created
        WHEN insert the product object into database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.create_new_product("mock_50", 50.0, "cpn_99")
        assert data.id == "mock_50"
        assert data.value == 50.0
        assert data.id_company == "cpn_99"

    def test_delete_company(self, configure_repo):
        """
        GIVEN a product object are in the database
        WHEN delete the product
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)
        """
        data = configure_repo.delete_product("fake-product_05")
        assert data == 1

    def test_update_product(self, configure_repo):
        """
        GIVEN a product is created
        WHEN update a product from the database
        THEN checks if the returned object from insert is equal to expected

        OBS: update() method is not testable with mock-alchemy, the return implemented is None.
        Issue: https://github.com/rajivsarvepalli/mock-alchemy/issues/161
        """
        data = configure_repo.update_product(
            "fake_company_20", "new_comp_value_10", 55.0
        )
        assert data is None

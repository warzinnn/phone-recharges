from typing import List

import pytest

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.domain.company import Company
from src.domain.products import Products
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.config.exceptions import (
    DataIsNotPresentInTable,
    EntityAlreadyExists,
)
from src.infrastructure.repository.products_repository import ProductsRepository


class FakeProductsRepository(ProductsRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_products(self) -> List[Products]:
        return [
            Products("vivo_10", 10.0, "vivo_11"),
            Products("claro_10", 10.0, "claro_11"),
            Products("claro_20", 20.0, "claro_11"),
            Products("claro_30", 30.0, "claro_11"),
            Products("oi_11", 11.0, "oi_11"),
        ]

    def select_product_by_id(self, product_id: str) -> List[Products]:
        pass

    def select_product_by_value(self, value: float) -> List[Products]:
        pass

    def select_products_by_company(self, company_id: str) -> List[Products]:
        return [Products("claro_10", 10.0, "claro_11")]

    def create_new_product(
        self, product_id: str, value: float, company_id: str
    ) -> Products:
        pass

    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        pass

    def delete_product(self, product_id: str) -> int:
        pass


@pytest.fixture(scope="class")
def configure_repo():
    """Fixture to return the ProductsRepository with the connection to DB"""
    return ProductsRepository(DBConnectionHandlerPostgre)


@pytest.fixture(scope="class")
def mock_data_for_products():
    """
    Fixture to insert a data into DB.
    After the test is done it will run the 'clean up', which deletes the objects inserted previoulsy
    """
    with DBConnectionHandlerPostgre() as db:
        try:
            company_data_insert = Company("mock_c_11")
            db.session.add(company_data_insert)
            data_insert = Products("mock_10", 10.0, "mock_c_11")
            db.session.add(data_insert)
            db.session.commit()
            yield
            db.session.delete(company_data_insert)
            db.session.delete(data_insert)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


@pytest.mark.usefixtures("set_mappers")
class TestProductsRepository:
    def test_select_all_products(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_products()
        assert isinstance(data[0], Products)

    def test_select_product_by_id(self, configure_repo, mock_data_for_products):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_id("mock_10")
        assert isinstance(data[0], Products)
        assert data[0].id == "mock_10"
        assert data[0].value == 10.0

    def test_select_product_by_id_fail(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_id("mock_1")
        assert isinstance(data, List)
        assert data == []

    def test_select_product_by_value(self, configure_repo, mock_data_for_products):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'value'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_value(10.0)
        assert isinstance(data[0], Products)
        assert isinstance(data[0].value, float)

    def test_select_product_by_value_fail(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'value' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_product_by_value(-1.0)
        assert isinstance(data, List)
        assert data == []

    def test_select_products_by_company(self, configure_repo, mock_data_for_products):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id_company'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_products_by_company("mock_c_11")
        assert isinstance(data[0], Products)
        assert data[0].id == "mock_10"
        assert data[0].value == 10.0
        assert data[0].id_company == "mock_c_11"

    def test_select_products_by_company_fail(self, configure_repo):
        """
        GIVEN a database with producties already inserted
        WHEN the select is realized with filter by 'id_company' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_products_by_company("mmm")
        assert isinstance(data, List)
        assert data == []

    def test_create_new_product(self, configure_repo):
        """
        GIVEN a product is created
        WHEN insert the product object into database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.create_new_product("mock_50", 50.0, "claro_11")
        assert isinstance(data, Products)
        assert data.id == "mock_50"

    def test_create_new_product_fail_product_already_exists(self, configure_repo):
        """
        GIVEN a product is created
        WHEN insert the product object into database
        THEN THEN checks if the error raised is equal to expected
        """
        with pytest.raises(EntityAlreadyExists) as e:
            configure_repo.create_new_product("mock_50", 50.0, "claro_11")
            assert str(e) == "Product already exists."

    def test_create_new_product_fail_company_does_not_exists(self, configure_repo):
        """
        GIVEN a product is created
        WHEN insert the product object into database
        THEN THEN checks if the error raised is equal to expected
        """
        with pytest.raises(DataIsNotPresentInTable) as e:
            configure_repo.create_new_product("mock_5", 50.0, "claro")
            assert str(e) == "Company does not exists."

    def test_update_product(self, configure_repo):
        """
        GIVEN a product is created
        WHEN update a product from the database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.update_product("claro_11", "mock_50", 50.5)
        assert data == 1

    def test_update_product_fail(self, configure_repo):
        """
        GIVEN a product is created
        WHEN update a product from the database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.update_product("claro", "mock_50", 50.5)
        data_two = configure_repo.update_product("claro_11", "mock_9999", 50.5)
        assert data == 0
        assert data_two == 0

    def test_delete_company(self, configure_repo):
        """
        GIVEN a product object are in the database
        WHEN delete the product
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)

        Obs: this test deletes the product created in the test 'test_create_new_product'
        """
        data = configure_repo.delete_product("mock_50")
        assert data == 1

    def test_delete_company_fail(self, configure_repo):
        """
        GIVEN a product object are in the database
        WHEN delete the product
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)

        Obs: this test deletes the product created in the test 'test_create_new_product'
        """
        data = configure_repo.delete_product("mmaaa")
        assert data == 0

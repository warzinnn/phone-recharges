from typing import List

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.use_cases.get_products.get_products_use_case import (
    GetProductsUseCase,
)
from src.domain.products import Products


class FakeProductsRepository(ProductsRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_products(self) -> List[Products]:
        return [
            Products("claro_10", 10.0, "claro_11"),
            Products("claro_20", 20.0, "claro_11"),
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


class TestGetProductsUseCase:
    def test_use_case_get_products(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns the products
        """
        repo = FakeProductsRepository()
        uc = GetProductsUseCase(repo)
        response_1 = uc.get_products("claro_11")
        response_2 = uc.get_products("")

        assert len(response_1) > 0
        assert response_1[0]["products"][0]["id"] == "claro_10"
        assert len(response_2) > 0
        assert response_2[0]["products"][1]["id"] == "claro_20"

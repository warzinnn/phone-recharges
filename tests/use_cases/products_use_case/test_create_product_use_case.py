from typing import List

from src.domain.model.products import Products
from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.create_product.create_product_use_case import CreateProductUseCase


class FakeProductsRepository(ProductsRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_products(self) -> List[Products]:
        pass

    def select_product_by_id(self, product_id: str) -> List[Products]:
        pass

    def select_product_by_value(self, value: float) -> List[Products]:
        pass

    def select_products_by_company(self, company_id: str) -> List[Products]:
        pass

    def create_new_product(
        self, product_id: str, value: float, company_id: str
    ) -> Products:
        return Products("claro_20", 20.0, "claro_11")

    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        pass

    def delete_product(self, product_id: str) -> int:
        pass


class TestCreateProductUseCase:
    def test_use_case_create_product(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a successful message
        """
        repo = FakeProductsRepository()
        uc = CreateProductUseCase()
        response = uc.create_product(repo, "claro_11", "claro_20", 20.0)

        assert response == "Product created"

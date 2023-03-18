from typing import List

from src.domain.model.products import Products
from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.update_product.update_product_use_case import UpdateProductUseCase


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
        pass

    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        return 1

    def delete_product(self, product_id: str) -> int:
        pass


class TestUpdateProductUseCase:
    def test_use_case_update_product(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a successful message
        """
        repo = FakeProductsRepository()
        uc = UpdateProductUseCase()
        response = uc.update_product(repo, "claro_11", "claro_20", 99.5)

        assert response == "Product updated"

from typing import List

from src.domain.model.products import Products
from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.delete_product.delete_product_use_case import DeleteProductUseCase


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
        pass

    def delete_product(self, product_id: str) -> int:
        return 1


class TestDeleteProductUseCase:
    def test_use_case_delete_product(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a successful message
        """
        repo = FakeProductsRepository()
        uc = DeleteProductUseCase()
        response = uc.delete_product(repo, "claro_20")

        assert response == "Product deleted"

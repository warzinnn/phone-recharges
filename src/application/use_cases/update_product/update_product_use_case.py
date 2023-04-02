from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.update_product_use_case_interface import (
    UpdateProductsUseCaseInterface,
)


class UpdateProductUseCase(UpdateProductsUseCaseInterface):
    """Class to define use_case: Update Product"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def update_product(
        self,
        company_id: str,
        product_id: str,
        product_value: float,
    ) -> str:
        """Update Product Use Case

        Args:
            company_id: company id
            product_id: product id
            product_value: product value
        Returns:
            str: message of resulting operation
        """
        data = self.repository.update_product(company_id, product_id, product_value)
        if data == 1:
            return "Product updated"

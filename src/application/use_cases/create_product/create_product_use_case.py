from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.create_product_use_case_interface import (
    CreateProductUseCaseInterface,
)
from src.domain.products import Products


class CreateProductUseCase(CreateProductUseCaseInterface):
    """Class to define use_case: Create Product"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def create_product(
        self,
        company_id: str,
        product_id: str,
        product_value: float,
    ) -> str:
        """Create Product Use Case

        Args:
            company_id: company id
            product_id: product id
            product_value: product value
        Returns:
            str: message of resulting operation
        """
        data = self.repository.create_new_product(product_id, product_value, company_id)
        if isinstance(data, Products):
            return "Product created"

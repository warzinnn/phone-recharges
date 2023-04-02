from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.delete_product_use_case_interface import (
    DeleteProductUseCaseInterface,
)


class DeleteProductUseCase(DeleteProductUseCaseInterface):
    """Class to define use_case: Delete Product"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def delete_product(self, product_id: str) -> str:
        """Delete Product Use Case

        Args:
            product_id: product id
        Returns:
            str: message of resulting operation
        """
        data = self.repository.delete_product(product_id)
        if data == 1:
            return "Product deleted"

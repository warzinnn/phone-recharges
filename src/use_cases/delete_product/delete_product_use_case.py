import re

from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class DeleteProductUseCase:
    """Class to define use_case: Delete Product"""

    def delete_product(self, repo: ProductsRepositoryInterface, product_id: str) -> str:
        """Delete Product Use Case

        Args:
            repo: Products Repository Interface
            product_id: product id
        Returns:
            str: message of resulting operation
        """
        if product_id:
            # data validation
            product_id = self.validate_product_id(product_id)

            data = repo.delete_product(product_id)
            if data == 1:
                return "Product deleted"

    def validate_product_id(self, product_id: str) -> str:
        """
        Auxiliar method to validate the product_id provided by the user
        Regex:
            matches any non-word character
        """
        regex_str = r"\W"
        input = re.search(regex_str, product_id)

        if input is None:
            if len(product_id) > 20:
                raise DataValidationError("Invalid product_id")
            else:
                return product_id
        else:
            raise DataValidationError("Invalid product_id")

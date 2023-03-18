import re

from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class UpdateProductUseCase:
    """Class to define use_case: Update Product"""

    def update_product(
        self,
        repo: ProductsRepositoryInterface,
        company_id: str,
        product_id: str,
        product_value: float,
    ) -> str:
        """Update Product Use Case

        Args:
            repo: Products Repository Interface
            company_id: company id
            product_id: product id
            product_value: product value
        Returns:
            str: message of resulting operation
        """
        if company_id and product_id and product_value:
            # data validation
            company_id = self.validate_company_id(company_id)
            product_id = self.validate_product_id(product_id)
            product_value = self.validate_value(product_value)

            data = repo.update_product(company_id, product_id, product_value)
            if data == 1:
                return "Product updated"
        return "Error"

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

    def validate_value(self, value: float) -> float:
        """
        Auxiliar method to validate the value provided by the user
        Regex:
            Match a single character not present in the list.
        """

        regex_str = r"[^0-9\.]"
        input = re.search(regex_str, str(value))

        if input is None:
            if float(value) < 0 or float(value) > 500:
                raise DataValidationError("Invalid value")
            else:
                return value
        else:
            raise DataValidationError("Invalid value")

    def validate_company_id(self, company_id: str) -> str:
        """
        Auxiliar method to validate the company_id provided by the user
        Regex:
            matches any non-word character
        """
        regex_str = r"\W"
        input = re.search(regex_str, company_id)

        if input is None:
            if len(company_id) > 20 or type(company_id) != str:
                raise DataValidationError("Invalid company_id")
            else:
                return company_id
        else:
            raise DataValidationError("Invalid company_id")

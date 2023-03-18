import re

from src.domain.model.products import Products
from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class CreateProductUseCase:
    """Class to define use_case: Create Product"""

    def create_product(
        self,
        repo: ProductsRepositoryInterface,
        company_id: str,
        product_id: str,
        product_value: float,
    ) -> str:
        """Create Product Use Case

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

            data = repo.create_new_product(product_id, product_value, company_id)
            if isinstance(data, Products):
                return "Product created"

    def validate_product_id(self, product_id: str) -> str:
        """
        Validates the product_id of the product.
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
        Validates the value of the product.
        Checks if the value is a number, and then check if its in the determined range.
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
        Validates the company_id.
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

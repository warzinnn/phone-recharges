import re

from src.application.interfaces.use_case_interfaces.update_product_use_case_interface import (
    UpdateProductsUseCaseInterface,
)
from src.application.presenters.http_model import HttpResponseModel
from src.application.use_cases.exceptions import DataValidationError


class UpdateProductController:
    """Class to define controller for use_case: update_product_use_case"""

    def __init__(self, use_case: UpdateProductsUseCaseInterface) -> None:
        self.use_case = use_case

    def handle(
        self, company_id: str, product_id: str, product_value: float
    ) -> HttpResponseModel:
        """Method to handle the call to use_case"""
        try:
            # input validation
            company_id = self.validate_company_id(company_id)
            product_id = self.validate_product_id(product_id)
            product_value = self.validate_value(product_value)

            # calling use_case
            data = self.use_case.update_product(
                company_id=company_id,
                product_id=product_id,
                product_value=product_value,
            )
            if data:
                return HttpResponseModel("Succeed", data, 200)
            return HttpResponseModel("Failed", "Error", 400)
        except DataValidationError as e:
            return HttpResponseModel("Failed", str(e), 400)
        except Exception:
            return HttpResponseModel("Failed", "Error", 500)

    def validate_product_id(self, product_id: str) -> str:
        """
        Auxiliar method to validate the product_id provided by the user

        Regex:
            matches any non-word character (raises an error).
        """
        regex_str = r"\W"
        input = re.search(regex_str, product_id)

        if input is not None or len(product_id) > 20 or len(product_id) == 0:
            raise DataValidationError("Invalid product_id")
        return product_id

    def validate_value(self, value: float) -> float:
        """
        Auxiliar method to validate the product_value provided by the user
        Checks if the value is a number, and then check if its in the determined range.

        Regex:
            Match a single character not present in the list.
        """

        regex_str = r"[^0-9\.]"
        input = re.search(regex_str, str(value))

        if input is not None or float(value) <= 0 or float(value) > 500:
            raise DataValidationError("Invalid product_value")
        return value

    def validate_company_id(self, company_id: str) -> str:
        """
        Auxiliar method to validate the company_id provided by the user

        Regex:
            matches any non-word character (raises an error).
        """
        regex_str = r"\W"
        input = re.search(regex_str, company_id)

        if input is not None or len(company_id) > 20 or len(company_id) == 0:
            raise DataValidationError("Invalid company_id")
        return company_id

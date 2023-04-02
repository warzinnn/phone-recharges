import re

from src.application.interfaces.use_case_interfaces.delete_product_use_case_interface import (
    DeleteProductUseCaseInterface,
)
from src.application.presenters.http_model import HttpResponseModel
from src.application.use_cases.exceptions import DataValidationError


class DeleteProductController:
    """Class to define controller for use_case: delete_product_use_case"""

    def __init__(self, use_case: DeleteProductUseCaseInterface) -> None:
        self.use_case = use_case

    def handle(self, product_id: str) -> HttpResponseModel:
        """Method to handle the call to use_case"""
        try:
            # input validation
            product_id = self.validate_product_id(product_id)

            # calling use_case
            data = self.use_case.delete_product(product_id=product_id)
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

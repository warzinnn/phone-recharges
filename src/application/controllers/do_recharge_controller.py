import re

from src.application.interfaces.use_case_interfaces.do_recharge_use_case_interface import (
    DoRechargeUseCaseInterface,
)
from src.application.presenters.http_model import HttpResponseModel
from src.application.use_cases.exceptions import DataValidationError


class DoRechargeController:
    """Class to define controller for use_case: do_recharge_use_case"""

    def __init__(self, use_case: DoRechargeUseCaseInterface) -> None:
        self.use_case = use_case

    def handle(self, phone_number: str, product_id: str) -> HttpResponseModel:
        """Method to handle the call to use_case"""
        try:
            # input validation
            phone_number = self.validate_phone_number(phone_number)
            product_id = self.validate_product_id(product_id)

            # calling use_case
            data = self.use_case.do_recharge(phone_number, product_id)
            if data:
                reponse_dict = {
                    "recharge_id": data.recharge_id,
                    "created_at": data.created_at,
                }
                return HttpResponseModel("Succeed", [reponse_dict], 200)
            return HttpResponseModel("Failed", "Error", 400)
        except DataValidationError as e:
            return HttpResponseModel("Failed", str(e), 400)
        except Exception:
            return HttpResponseModel("Failed", "Error", 500)

    def validate_phone_number(self, phone_number: str) -> str:
        """
        Auxiliar method to validate the phone_number provided by the user

        Regex:
            matches any character that's not a digit
        """
        regex_str = r"\D"
        input = re.search(regex_str, phone_number)

        if input is not None or len(phone_number) > 13 or len(phone_number) == 0:
            raise DataValidationError("Invalid phone_number")
        return phone_number

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

import re

from src.application.interfaces.use_case_interfaces.get_recharges_use_case_interface import (
    GetRechargesUseCaseInterface,
)
from src.application.presenters.http_model import HttpResponseModel
from src.application.use_cases.exceptions import DataValidationError


class GetRechargesController:
    """Class to define controller for use_case: get_recharges_use_case"""

    def __init__(self, use_case: GetRechargesUseCaseInterface) -> None:
        self.use_case = use_case

    def handle(self, recharge_id: str, phone_number: str) -> HttpResponseModel:
        """Method to handle the call to use_case"""
        try:
            if recharge_id:
                recharge_id = self.validate_recharge_id(recharge_id)
                data = self.use_case.get_recharges(
                    recharge_id=recharge_id, phone_number=""
                )
                if data == []:
                    return HttpResponseModel(
                        "Failed", "recharge_id does not exist", 200
                    )
                return HttpResponseModel("Succeed", data, 200)
            elif phone_number:
                phone_number = self.validate_phone_number(phone_number)
                data = self.use_case.get_recharges(
                    recharge_id="", phone_number=phone_number
                )
                if data == []:
                    return HttpResponseModel(
                        "Failed", "phone_number does not exist", 200
                    )
                return HttpResponseModel("Succeed", data, 200)
            else:
                data = self.use_case.get_recharges("", "")
                return HttpResponseModel("Succeed", data, 200)
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

        if input is not None or len(phone_number) > 13:
            raise DataValidationError("Invalid phone_number")
        return phone_number

    def validate_recharge_id(self, recharge_id: str) -> str:
        """
        Auxiliar method to validate the recharge_id provided by the user

        Regex:
            Matches everything that is different from this range [^a-zA-Z0-9_-]
        """
        regex_str = r"[^a-zA-Z0-9-]"
        input = re.search(regex_str, recharge_id)

        if input is not None or len(recharge_id) > 36:
            raise DataValidationError("Invalid recharge_id")
        return recharge_id

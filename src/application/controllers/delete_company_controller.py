import re

from src.application.interfaces.use_case_interfaces.delete_company_use_case_interface import (
    DeleteCompanyUseCaseInterface,
)
from src.application.presenters.http_model import HttpResponseModel
from src.application.use_cases.exceptions import DataValidationError


class DeleteCompanyController:
    """Class to define controller for use_case: delete_company_use_case"""

    def __init__(self, use_case: DeleteCompanyUseCaseInterface) -> None:
        self.use_case = use_case

    def handle(self, company_id: str) -> HttpResponseModel:
        """Method to handle the call to use_case"""
        try:
            company_id = self.validate_company_id(company_id)
            data = self.use_case.delete_company(company_id=company_id)
            if data:
                return HttpResponseModel("Succeed", data, 200)
            return HttpResponseModel("Failed", "Error", 400)
        except DataValidationError as e:
            return HttpResponseModel("Failed", str(e), 400)
        except Exception:
            return HttpResponseModel("Failed", "Error", 500)

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

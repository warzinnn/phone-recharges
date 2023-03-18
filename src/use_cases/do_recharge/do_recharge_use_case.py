import re

from src.domain.model.recharge import Recharge
from src.interfaces.recharges_repository_interface import RechargesRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class DoRechargeUseCase:
    """Class to define use_case: Do Recharge"""

    def do_recharge(
        self, repo: RechargesRepositoryInterface, phone_number: str, product_id: str
    ) -> Recharge:
        """Do Recharge Use Case

        Args:
            repo: Recharges Repository Interface
            product_id: product id
            phone_number: phone number
        Returns:
            Recharge: Recharge object
        """
        if product_id and phone_number:
            product_id = self.validate_product_id(product_id)
            phone_number = self.validate_phone_number(phone_number)

            data = repo.do_recharge(phone_number, product_id)
            return data

    def validate_phone_number(self, phone_number: str) -> str:
        """
        Auxiliar method to validate the phone_number provided by the user

        Regex:
            matches any character that's not a digit
        """
        regex_str = r"\D"
        input = re.search(regex_str, phone_number)

        if input is None:
            if len(phone_number) > 13:
                raise DataValidationError("Invalid phone_number")
            else:
                return phone_number
        else:
            raise DataValidationError("Invalid phone_number")

    def validate_product_id(self, product_id: str) -> str:
        """
        Auxiliar method to validate the product_id provided by the user

        Regex:
            Everything that is different from this range [^a-zA-Z0-9_] will raise an error.
        """
        regex_str = r"\W"
        input = re.search(regex_str, product_id)

        if input is None:
            if len(product_id) > 20 or type(product_id) != str:
                raise DataValidationError("Invalid product_id")
            else:
                return product_id
        else:
            raise DataValidationError("Invalid product_id")

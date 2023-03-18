import re
from typing import List

from src.domain.model.recharge import Recharge
from src.interfaces.recharges_repository_interface import RechargesRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class GetRechargesUseCase:
    """Class to define use_case: Get Recharges"""

    def get_recharges(
        self, repo: RechargesRepositoryInterface, recharge_id: str, phone_number: str
    ) -> List[Recharge]:
        """Get Recharges Use Case

        Args:
            repo: Recharges Repository Interface
            company_id: company id
        Returns:
            List[Recharge]: List with companies
        """
        if recharge_id:
            recharge_id = self.validate_recharge_id(recharge_id)
            data = repo.select_all_recharges_by_recharge_id(recharge_id)
        elif phone_number:
            phone_number = self.validate_phone_number(phone_number)
            data = repo.select_all_recharges_by_phone_number(phone_number)
        else:
            data = repo.select_all_recharges()

        response = []
        for entry in data:
            tmp_dict = entry[0].as_dict()
            tmp_dict["company_id"] = entry[2]
            tmp_dict["value"] = entry[1]
            response.append(tmp_dict)
        return response

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

    def validate_recharge_id(self, recharge_id: str) -> str:
        """
        Auxiliar method to validate the recharge_id provided by the user
        Regex:
            Matches everything that is different from this range [^a-zA-Z0-9_-]
        """
        regex_str = r"[^a-zA-Z0-9-]"
        input = re.search(regex_str, recharge_id)

        if input is None:
            if len(recharge_id) > 36:
                raise DataValidationError("Invalid recharge_id")
            else:
                return recharge_id
        else:
            raise DataValidationError("Invalid recharge_id")

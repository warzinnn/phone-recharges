from typing import List

from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_recharges_use_case_interface import (
    GetRechargesUseCaseInterface,
)
from src.domain.recharge import Recharge


class GetRechargesUseCase(GetRechargesUseCaseInterface):
    """Class to define use_case: Get Recharges"""

    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        self.repository = repository

    def get_recharges(self, recharge_id: str, phone_number: str) -> List[Recharge]:
        """Get Recharges Use Case

        Args:
            recharge_id: id of recharge
            phone_number: phone number
        Returns:
            List[Recharge]: List with recharges
        """
        if recharge_id:
            data = self.repository.select_all_recharges_by_recharge_id(recharge_id)
        elif phone_number:
            data = self.repository.select_all_recharges_by_phone_number(phone_number)
        else:
            data = self.repository.select_all_recharges()

        # format data
        response = []
        for entry in data:
            tmp_dict = entry[0].as_dict()
            tmp_dict["company_id"] = entry[2]
            tmp_dict["value"] = entry[1]
            response.append(tmp_dict)

        return response

from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.do_recharge_use_case_interface import (
    DoRechargeUseCaseInterface,
)
from src.domain.recharge import Recharge


class DoRechargeUseCase(DoRechargeUseCaseInterface):
    """Class to define use_case: Do Recharge"""

    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        self.repository = repository

    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        """Do Recharge Use Case

        Args:
            product_id: product id
            phone_number: phone number
        Returns:
            Recharge: Recharge object
        """
        data = self.repository.do_recharge(phone_number, product_id)
        return data

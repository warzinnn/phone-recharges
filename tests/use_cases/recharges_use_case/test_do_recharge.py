from typing import List

from src.domain.model.recharge import Recharge
from src.interfaces.recharges_repository_interface import RechargesRepositoryInterface
from src.use_cases.do_recharge.do_recharge_use_case import DoRechargeUseCase


class FakeProductsRepository(RechargesRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_recharges(self) -> List:
        pass

    def select_all_recharges_by_recharge_id(self, recharge_id: str) -> List:
        pass

    def select_all_recharges_by_phone_number(self, phone_number: str) -> List:
        pass

    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        return Recharge("5511999999999", "claro_50")


class TestDoRechargeUseCase:
    def test_use_case_do_recharge(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a Recharge Object
        """
        repo = FakeProductsRepository()
        uc = DoRechargeUseCase()

        response = uc.do_recharge(repo, "5511999999999", "claro_50")

        assert isinstance(response, Recharge)

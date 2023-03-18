from typing import List

from src.domain.model.recharge import Recharge
from src.interfaces.recharges_repository_interface import RechargesRepositoryInterface
from src.use_cases.get_recharges.get_recharges_use_case import GetRechargesUseCase


class FakeProductsRepository(RechargesRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_recharges(self) -> List:
        return [
            (Recharge("5511999999999", "claro_50"), 50.0, "claro_11"),
            (Recharge("5511999999999", "claro_10"), 10.0, "claro_11"),
        ]

    def select_all_recharges_by_recharge_id(self, recharge_id: str) -> List:
        return [
            (Recharge("5511999999999", "claro_50"), 50.0, "claro_11"),
            (Recharge("5511999999999", "claro_10"), 10.0, "claro_11"),
        ]

    def select_all_recharges_by_phone_number(self, phone_number: str) -> List:
        return [
            (Recharge("5511999999999", "claro_50"), 50.0, "claro_11"),
            (Recharge("5511999999999", "claro_10"), 10.0, "claro_11"),
        ]

    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        pass


class TestGetRechargesUseCase:
    def test_use_case_get_recharges(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a List with a Tuple object
        """
        repo = FakeProductsRepository()
        uc = GetRechargesUseCase()

        response_1 = uc.get_recharges(repo, "", "")
        response_2 = uc.get_recharges(repo, "eedbcbef-a8e9-44ef-a920-289ca663e552", "")
        response_3 = uc.get_recharges(repo, "", "5511999999999")

        assert len(response_1) > 0
        assert response_1[0]["phone_number"] == "5511999999999"
        assert response_1[0]["value"] == 50.0
        assert len(response_2) > 0
        assert response_1[0]["phone_number"] == "5511999999999"
        assert response_1[0]["value"] == 50.0
        assert len(response_3) > 0
        assert response_1[0]["phone_number"] == "5511999999999"
        assert response_1[0]["value"] == 50.0

from typing import List

import pytest

from src.application.controllers.get_recharges_controller import GetRechargesController
from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_recharges_use_case_interface import (
    GetRechargesUseCaseInterface,
)
from src.domain.recharge import Recharge


class FakeCompanyUseCase(GetRechargesUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        pass

    def get_recharges(self, recharge_id: str, phone_number: str) -> List[Recharge]:
        # simple if else to simulate flows
        if (
            phone_number == "5511999999991"
            or recharge_id == "999284e1-1ef0-4c31-9c1b-e9fcdfabc999"
        ):
            return []
        else:
            return [
                {
                    "recharge_id": "51b284e1-1ef0-4c31-9c1b-e9fcdfabc141",
                    "created_at": "2023-03-17 19:10:30.73952",
                    "phone_number": "5511999999999",
                    "product_id": "claro_50",
                    "company_id": "claro_11",
                    "value": 50.0,
                },
                {
                    "recharge_id": "e44653d7-9b7c-404a-b32f-46d6cd7d006d",
                    "created_at": "2023-03-17 19:10:24.013",
                    "phone_number": "5511999999999",
                    "product_id": "claro_50",
                    "company_id": "claro_11",
                    "value": 50.0,
                },
            ]


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestGetRechargesController:
    def test_get_recharges_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("", "5511999999999")

        assert response.data[0]["recharge_id"] == "51b284e1-1ef0-4c31-9c1b-e9fcdfabc141"
        assert response.data[1]["recharge_id"] == "e44653d7-9b7c-404a-b32f-46d6cd7d006d"

    def test_get_recharge_id_controller_with_invalid_recharge_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("eedbcbef%^#$%#", "")

        assert response.data == "Invalid recharge_id"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_with_long_recharge_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetRechargesController(use_case)
        response = controller.handle(
            "eedbcbef-a8e9-44ef-a920-289ca663e552eedbcbef-a8e9-44ef-a920-289ca663e552",
            "",
        )

        assert response.data == "Invalid recharge_id"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_with_invalid_phone_number_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("", "a88@#$@#$@#$")

        assert response.data == "Invalid phone_number"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_with_long_phone_number_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("", "12312312312312312312312312321312312")

        assert response.data == "Invalid phone_number"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_phone_number_does_not_exist(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the inexistence of phone number
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("", "5511999999991")

        assert response.data == "phone_number does not exist"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_recharge_id_does_not_exist(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the inexistence of recharge_id
        """
        controller = GetRechargesController(use_case)
        response = controller.handle("999284e1-1ef0-4c31-9c1b-e9fcdfabc999", "")

        assert response.data == "recharge_id does not exist"
        assert response.message == "Failed"

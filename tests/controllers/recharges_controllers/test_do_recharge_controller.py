import uuid

import pytest

from src.application.controllers.do_recharge_controller import DoRechargeController
from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.do_recharge_use_case_interface import (
    DoRechargeUseCaseInterface,
)
from src.domain.recharge import Recharge


class FakeCompanyUseCase(DoRechargeUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        pass

    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        return Recharge("5511999999999", "claro_50")


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestDoRechargeController:
    def test_do_recharge_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = DoRechargeController(use_case)
        response = controller.handle("5511999999999", "claro_50")

        assert isinstance(response.data[0]["recharge_id"], uuid.UUID)
        assert response.message == "Succeed"

    def test_do_recharge_controller_with_invalid_phone_number_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DoRechargeController(use_case)
        response = controller.handle("a88@#$@#$@#$", "claro_50")

        assert response.data == "Invalid phone_number"
        assert response.message == "Failed"

    def test_do_recharge_controller_with_long_phone_number_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DoRechargeController(use_case)
        response = controller.handle("12312312312312312312312312321312312", "claro_50")

        assert response.data == "Invalid phone_number"
        assert response.message == "Failed"

    def test_do_recharge_controller_with_invalid_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DoRechargeController(use_case)
        response = controller.handle("5511999999999", "a88@#$@#$@#$")

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_get_recharge_id_controller_with_long_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DoRechargeController(use_case)
        response = controller.handle(
            "5511999999999", "12312312312312312312312312321312312"
        )

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

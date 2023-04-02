import pytest

from src.application.controllers.get_company_controller import GetCompanyController
from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_company_use_case_interface import (
    GetCompanyUseCaseInterface,
)
from src.domain.company import Company


class FakeCompanyUseCase(GetCompanyUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        pass

    def get_company(self, company_id: str) -> str:
        if company_id == "mock_10":
            return []
        return [Company("5ca667f8"), Company("472af23a")]


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestGetCompanyController:
    def test_get_company_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = GetCompanyController(use_case)
        response = controller.handle("")

        assert response.data[0].company_id == "5ca667f8"
        assert response.data[1].company_id == "472af23a"
        assert response.message == "Succeed"

    def test_get_company_controller_with_invalid_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetCompanyController(use_case)
        response = controller.handle("test_1%")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_get_company_controller_with_long_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetCompanyController(use_case)
        response = controller.handle("2400a00k12312312312312312321")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_get_company_controller_with_company_id_that_does_not_exist_fail(
        self, use_case
    ):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the inexistence of recharge_id
        """
        controller = GetCompanyController(use_case)
        response = controller.handle("mock_10")

        assert response.data == "company_id does not exist"
        assert response.message == "Failed"

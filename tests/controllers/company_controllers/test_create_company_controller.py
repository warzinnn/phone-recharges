import pytest

from src.application.controllers.create_company_controller import (
    CreateCompanyController,
)
from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.create_company_use_case_interface import (
    CreateCompanyUseCaseInterface,
)


class FakeCompanyUseCase(CreateCompanyUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        pass

    def create_company(self, company_id: str) -> str:
        return "Company created"


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestCreateCompanyController:
    def test_create_company_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = CreateCompanyController(use_case)
        response = controller.handle("test_1")

        assert response.data == "Company created"
        assert response.message == "Succeed"

    def test_create_company_controller_with_invalid_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = CreateCompanyController(use_case)
        response = controller.handle("test_1%")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_create_company_controller_with_long_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = CreateCompanyController(use_case)
        response = controller.handle("2400a00k12312312312312312321")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_create_company_controller_with_empty_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = CreateCompanyController(use_case)
        response = controller.handle("")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

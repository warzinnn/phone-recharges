import pytest

from src.application.controllers.delete_company_controller import (
    DeleteCompanyController,
)
from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.delete_company_use_case_interface import (
    DeleteCompanyUseCaseInterface,
)


class FakeCompanyUseCase(DeleteCompanyUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        pass

    def delete_company(self, company_id: str) -> str:
        return "Company deleted"


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestDeleteCompanyController:
    def test_delete_company_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = DeleteCompanyController(use_case)
        response = controller.handle("test_1")

        assert response.data == "Company deleted"
        assert response.message == "Succeed"

    def test_delete_company_controller_with_invalid_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteCompanyController(use_case)
        response = controller.handle("test_1%")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_delete_company_controller_with_long_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteCompanyController(use_case)
        response = controller.handle("2400a00k12312312312312312321")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_delete_company_controller_with_empty_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteCompanyController(use_case)
        response = controller.handle("")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

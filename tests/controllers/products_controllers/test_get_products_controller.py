import pytest

from src.application.controllers.get_products_controller import GetProductsController
from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_products_use_case_interface import (
    GetProductsUseCaseInterface,
)
from src.domain.products import Products


class FakeCompanyUseCase(GetProductsUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        pass

    def get_products(self, company_id: str) -> str:
        if company_id == "mock_10":
            return []
        return [
            Products("claro_10", 10.0, "claro_11"),
            Products("claro_20", 20.0, "claro_11"),
        ]


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestGetProductController:
    def test_get_product_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = GetProductsController(use_case)
        response = controller.handle("")

        assert response.data[0].id == "claro_10"
        assert response.data[1].id == "claro_20"
        assert response.message == "Succeed"

    def test_get_products_controller_with_invalid_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetProductsController(use_case)
        response = controller.handle("test_1%")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_get_products_controller_with_long_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = GetProductsController(use_case)
        response = controller.handle("2400a00k12312312312312312321")

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_get_products_controller_with_company_id_that_does_not_exist_fail(
        self, use_case
    ):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the inexistence of recharge_id
        """
        controller = GetProductsController(use_case)
        response = controller.handle("mock_10")

        assert response.data == "company_id does not exist"
        assert response.message == "Failed"

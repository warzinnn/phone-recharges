import pytest

from src.application.controllers.update_product_controller import (
    UpdateProductController,
)
from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.update_product_use_case_interface import (
    UpdateProductsUseCaseInterface,
)


class FakeCompanyUseCase(UpdateProductsUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        pass

    def update_product(
        self,
        company_id: str,
        product_id: str,
        product_value: float,
    ) -> str:
        return "Product updated"


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestUpdateProductController:
    def test_update_product_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11", "claro_20", 99.5)
        assert response.data == "Product updated"
        assert response.message == "Succeed"

    def test_update_product_controller_with_invalid_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11@#$@#$", "claro_20", 99.5)

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_empty_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("", "claro_20", 99.5)

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_long_company_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_1111111111111111", "claro_20", 99.5)

        assert response.data == "Invalid company_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_invalid_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11", "claro_20@#$@#$", 99.5)

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_empty_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11", "", 99.5)

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_long_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11", "claro_200000000000000000", 99.5)

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_update_product_controller_with_invalid_range_value(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response_1 = controller.handle("claro_11", "claro_20", 0)
        response_2 = controller.handle("claro_11", "claro_20", -1)
        response_3 = controller.handle("claro_11", "claro_20", 501)

        assert response_1.data == "Invalid product_value"
        assert response_2.data == "Invalid product_value"
        assert response_3.data == "Invalid product_value"

    def test_update_product_controller_with_invalid_value(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = UpdateProductController(use_case)
        response = controller.handle("claro_11", "claro_20", "123asdasd")

        assert response.data == "Invalid product_value"
        assert response.message == "Failed"

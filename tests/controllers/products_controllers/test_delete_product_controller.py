import pytest

from src.application.controllers.delete_product_controller import (
    DeleteProductController,
)
from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.delete_product_use_case_interface import (
    DeleteProductUseCaseInterface,
)


class FakeCompanyUseCase(DeleteProductUseCaseInterface):
    """Fake Use_Case for Tests"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        pass

    def delete_product(self, product_id: str) -> str:
        return "Product deleted"


@pytest.fixture
def use_case():
    """Fixture to initialize use_case"""
    use_case = FakeCompanyUseCase("FakeRepo")
    return use_case


class TestDeleteProductController:
    def test_delete_product_controller(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a successful message
        """
        controller = DeleteProductController(use_case)
        response = controller.handle("test_11")
        assert response.data == "Product deleted"
        assert response.message == "Succeed"

    def test_delete_product_controller_with_invalid_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteProductController(use_case)
        response = controller.handle("claro_11%$#&")

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_delete_product_controller_with_empty_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteProductController(use_case)
        response = controller.handle("")

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

    def test_delete_product_controller_with_long_product_id_fail(self, use_case):
        """
        GIVEN a controller is proper implemented
        WHEN the controller is required
        THEN checks if the implementation returns a failed message due to the input validation
        """
        controller = DeleteProductController(use_case)
        response = controller.handle("claro_200000000000000000")

        assert response.data == "Invalid product_id"
        assert response.message == "Failed"

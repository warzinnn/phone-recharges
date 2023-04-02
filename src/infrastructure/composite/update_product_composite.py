from src.application.controllers.update_product_controller import (
    UpdateProductController,
)
from src.application.use_cases.update_product.update_product_use_case import (
    UpdateProductUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.products_repository import ProductsRepository


def update_product_composite() -> UpdateProductController:
    """Composing UpdateProductController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: ProductsRepository
        use_case: UpdateProductUseCase

    Args:
        None
    Returns:
        UpdateProductController: instance of UpdateProductController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = ProductsRepository(db_connection)
    use_case = UpdateProductUseCase(repository)

    controller = UpdateProductController(use_case)
    return controller

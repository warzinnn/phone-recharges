from src.application.controllers.get_products_controller import GetProductsController
from src.application.use_cases.get_products.get_products_use_case import (
    GetProductsUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.products_repository import ProductsRepository


def get_products_composite() -> GetProductsController:
    """Composing GetProductsController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: ProductsRepository
        use_case: GetProductsUseCase

    Args:
        None
    Returns:
        GetProductsController: instance of GetProductsController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = ProductsRepository(db_connection)
    use_case = GetProductsUseCase(repository)

    controller = GetProductsController(use_case)
    return controller

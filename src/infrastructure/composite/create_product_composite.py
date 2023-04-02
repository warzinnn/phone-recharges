from src.application.controllers.create_product_controller import (
    CreateProductController,
)
from src.application.use_cases.create_product.create_product_use_case import (
    CreateProductUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.products_repository import ProductsRepository


def create_product_composite() -> CreateProductController:
    """Composing CreateProductController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: ProductsRepository
        use_case: CreateProductUseCase

    Args:
        None
    Returns:
        CreateProductController: instance of CreateProductController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = ProductsRepository(db_connection)
    use_case = CreateProductUseCase(repository)

    controller = CreateProductController(use_case)
    return controller

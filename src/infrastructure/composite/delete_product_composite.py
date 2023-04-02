from src.application.controllers.delete_product_controller import (
    DeleteProductController,
)
from src.application.use_cases.delete_product.delete_product_use_case import (
    DeleteProductUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.products_repository import ProductsRepository


def delete_product_composite() -> DeleteProductController:
    """Composing DeleteProductController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: CompanyRepository
        use_case: DeleteCompanyUseCase

    Args:
        None
    Returns:
        DeleteProductController: instance of DeleteProductController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = ProductsRepository(db_connection)
    use_case = DeleteProductUseCase(repository)

    controller = DeleteProductController(use_case)
    return controller

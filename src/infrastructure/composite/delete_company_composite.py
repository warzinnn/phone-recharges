from src.application.controllers.delete_company_controller import (
    DeleteCompanyController,
)
from src.application.use_cases.delete_company.delete_company_use_case import (
    DeleteCompanyUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.company_repository import CompanyRepository


def delete_company_composite() -> DeleteCompanyController:
    """Composing DeleteCompanyController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: CompanyRepository
        use_case: DeleteCompanyUseCase

    Args:
        None
    Returns:
        DeleteCompanyController: instance of DeleteCompanyController
    """

    db_connection = DBConnectionHandlerPostgre
    company_repository = CompanyRepository(db_connection)
    use_case = DeleteCompanyUseCase(company_repository)

    controller = DeleteCompanyController(use_case)
    return controller

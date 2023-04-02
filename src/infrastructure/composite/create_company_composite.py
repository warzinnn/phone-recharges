from src.application.controllers.create_company_controller import (
    CreateCompanyController,
)
from src.application.use_cases.create_company.create_company_use_case import (
    CreateCompanyUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.company_repository import CompanyRepository


def create_company_composite() -> CreateCompanyController:
    """Composing CreateCompanyController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: CompanyRepository
        use_case: CreateCompanyUseCase

    Args:
        None
    Returns:
        CreateCompanyController: instance of CreateCompanyController
    """

    db_connection = DBConnectionHandlerPostgre
    company_repository = CompanyRepository(db_connection)
    use_case = CreateCompanyUseCase(company_repository)

    controller = CreateCompanyController(use_case)
    return controller

from src.application.controllers.get_company_controller import GetCompanyController
from src.application.use_cases.get_company.get_company_use_case import GetCompanyUseCase
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.company_repository import CompanyRepository


def get_company_composite() -> GetCompanyController:
    """Composing GetCompanyController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: CompanyRepository
        use_case: GetCompanyUseCase

    Args:
        None
    Returns:
        GetCompanyController: instance of GetCompanyController
    """

    db_connection = DBConnectionHandlerPostgre
    company_repository = CompanyRepository(db_connection)
    use_case = GetCompanyUseCase(company_repository)

    controller = GetCompanyController(use_case)
    return controller

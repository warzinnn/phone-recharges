from src.application.controllers.get_recharges_controller import GetRechargesController
from src.application.use_cases.get_recharges.get_recharges_use_case import (
    GetRechargesUseCase,
)
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.recharges_repository import RechargeRepository


def get_recharges_composite() -> GetRechargesController:
    """Composing GetRechargesController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: RechargeRepository
        use_case: GetRechargesUseCase

    Args:
        None
    Returns:
        GetRechargesController: instance of GetRechargesController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = RechargeRepository(db_connection)
    use_case = GetRechargesUseCase(repository)

    controller = GetRechargesController(use_case)
    return controller

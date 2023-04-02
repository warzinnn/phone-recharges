from src.application.controllers.do_recharge_controller import DoRechargeController
from src.application.use_cases.do_recharge.do_recharge_use_case import DoRechargeUseCase
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.repository.recharges_repository import RechargeRepository


def do_recharge_composite() -> DoRechargeController:
    """Composing DoRechargeController

    Uses:
        db_connection: DBConnectionHandlerPostgre
        repository: RechargeRepository
        use_case: DoRechargeUseCase

    Args:
        None
    Returns:
        DoRechargeController: instance of DoRechargeController
    """

    db_connection = DBConnectionHandlerPostgre
    repository = RechargeRepository(db_connection)
    use_case = DoRechargeUseCase(repository)

    controller = DoRechargeController(use_case)
    return controller

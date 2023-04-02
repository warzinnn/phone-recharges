from abc import ABC, abstractmethod

from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.domain.recharge import Recharge


class DoRechargeUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        raise NotImplementedError

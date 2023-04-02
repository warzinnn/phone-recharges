from abc import ABC, abstractmethod
from typing import List

from src.application.interfaces.repository_interfaces.recharges_repository_interface import (
    RechargesRepositoryInterface,
)
from src.domain.recharge import Recharge


class GetRechargesUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: RechargesRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_recharges(self, recharge_id: str, phone_number: str) -> List[Recharge]:
        raise NotImplementedError

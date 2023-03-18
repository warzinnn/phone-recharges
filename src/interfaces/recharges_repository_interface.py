from abc import ABC, abstractmethod
from typing import List

from src.domain.model.recharge import Recharge


class RechargesRepositoryInterface(ABC):
    @abstractmethod
    def select_all_recharges(self) -> List:
        raise NotImplementedError

    @abstractmethod
    def select_all_recharges_by_recharge_id(self, recharge_id: str) -> List:
        raise NotImplementedError

    @abstractmethod
    def select_all_recharges_by_phone_number(self, phone_number: str) -> List:
        raise NotImplementedError

    @abstractmethod
    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        raise NotImplementedError

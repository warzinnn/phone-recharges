from abc import ABC, abstractmethod
from typing import List

from src.domain.company import Company


class CompanyRepositoryInterface(ABC):
    @abstractmethod
    def select_all_company(self) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def select_company_by_id(self, company_id: str) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def create_new_company(self, company_id: str) -> Company:
        raise NotImplementedError

    @abstractmethod
    def delete_company(self, company_id: str) -> int:
        raise NotImplementedError

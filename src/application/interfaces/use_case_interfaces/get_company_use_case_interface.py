from abc import ABC, abstractmethod
from typing import List

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.domain.company import Company


class GetCompanyUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_company(self, company_id: str) -> List[Company]:
        raise NotImplementedError

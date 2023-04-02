from abc import ABC, abstractmethod

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)


class CreateCompanyUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_company(self, company_id: str) -> str:
        raise NotImplementedError

from typing import List

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_company_use_case_interface import (
    GetCompanyUseCaseInterface,
)
from src.domain.company import Company


class GetCompanyUseCase(GetCompanyUseCaseInterface):
    """Class to define use_case: Get Company"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        self.repository = repository

    def get_company(self, company_id: str) -> List[Company]:
        """Get Company Use Case

        Args:
            company_id: company id
        Returns:
            List[Company]: List with companies
        """
        if company_id:
            data = self.repository.select_company_by_id(company_id)
        else:
            data = self.repository.select_all_company()

        if isinstance(data, List):
            response = [i.company_as_dict() for i in data]
            return response

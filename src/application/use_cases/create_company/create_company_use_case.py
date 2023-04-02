from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.create_company_use_case_interface import (
    CreateCompanyUseCaseInterface,
)
from src.domain.company import Company


class CreateCompanyUseCase(CreateCompanyUseCaseInterface):
    """Class to define use_case: Create Company"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        self.repository = repository

    def create_company(self, company_id: str) -> str:
        """Create Company Use Case

        Args:
            company_id: company id
        Returns:
            str: message of resulting operation
        """
        data = self.repository.create_new_company(company_id)
        if isinstance(data, Company):
            return "Company created"

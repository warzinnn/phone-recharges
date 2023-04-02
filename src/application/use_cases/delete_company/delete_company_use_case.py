from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.delete_company_use_case_interface import (
    DeleteCompanyUseCaseInterface,
)


class DeleteCompanyUseCase(DeleteCompanyUseCaseInterface):
    """Class to define use_case: Delete Company"""

    def __init__(self, repository: CompanyRepositoryInterface) -> None:
        self.repository = repository

    def delete_company(self, company_id: str) -> str:
        """Delete Company Use Case

        Args:
            company_id: company id
        Returns:
            str: message of resulting operation
        """
        data = self.repository.delete_company(company_id)
        if data == 1:
            return "Company deleted"

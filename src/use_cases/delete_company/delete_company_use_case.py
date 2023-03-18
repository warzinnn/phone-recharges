import re

from src.interfaces.company_repository_interface import CompanyRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class DeleteCompanyUseCase:
    """Class to define use_case: Delete Company"""

    def delete_company(self, repo: CompanyRepositoryInterface, company_id: str) -> str:
        """Delete Company Use Case

        Args:
            repo: Company Repository Interface
            company_id: company id
        Returns:
            str: message of resulting operation
        """
        if company_id:
            company_id = self.validate_company_id(company_id)
            data = repo.delete_company(company_id)
        if data == 1:
            return "Company deleted"

    def validate_company_id(self, company_id: str):
        """
        Auxiliar method to validate the company_id provided by the user

        Regex:
            matches any non-word character.
        """
        regex_str = r"\W"
        input = re.search(regex_str, company_id)

        if input is None:
            if len(company_id) > 20:
                raise DataValidationError("Invalid company_id")
            else:
                return company_id
        else:
            raise DataValidationError("Invalid company_id")

import re
from typing import List

from src.domain.model.company import Company
from src.interfaces.company_repository_interface import CompanyRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class GetCompanyUseCase:
    """Class to define use_case: Get Company"""

    def get_company(
        self, repo: CompanyRepositoryInterface, company_id: str
    ) -> List[Company]:
        """Get Company Use Case

        Args:
            repo: Company Repository Interface
            company_id: company id
        Returns:
            List[Company]: List with companies
        """
        if company_id:
            company_id = self.validate_company_id(company_id)
            data = repo.select_company_by_id(company_id)
        else:
            data = repo.select_all_company()

        response = [i.company_as_dict() for i in data]
        return response

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

from typing import List

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.use_cases.delete_company.delete_company_use_case import (
    DeleteCompanyUseCase,
)
from src.domain.company import Company


class FakeCompanyRepository(CompanyRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_company(self) -> List[Company]:
        pass

    def select_company_by_id(self, company_id: str) -> List[Company]:
        pass

    def create_new_company(self, company_id: str) -> Company:
        pass

    def delete_company(self, company_id: str) -> int:
        return 1


class TestDeleteCompanyUseCase:
    def test_use_case_delete_company(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation deletes a company successfully
        """
        repo = FakeCompanyRepository()
        uc = DeleteCompanyUseCase(repo)
        response = uc.delete_company("2400a00k")

        assert response == "Company deleted"

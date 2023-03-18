from typing import List

from src.domain.model.company import Company
from src.interfaces.company_repository_interface import CompanyRepositoryInterface
from src.use_cases.delete_company.delete_company_use_case import DeleteCompanyUseCase


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
        uc = DeleteCompanyUseCase()
        response = uc.delete_company(repo, "2400a00k")

        assert response == "Company deleted"

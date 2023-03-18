from typing import List

from src.domain.model.company import Company
from src.interfaces.company_repository_interface import CompanyRepositoryInterface
from src.use_cases.create_company.create_company_use_case import CreateCompanyUseCase


class FakeCompanyRepository(CompanyRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_company(self) -> List[Company]:
        pass

    def select_company_by_id(self, company_id: str) -> List[Company]:
        pass

    def create_new_company(self, company_id: str) -> Company:
        return Company("2400a00k")

    def delete_company(self, company_id: str) -> int:
        pass


class TestCreateCompanyUseCase:
    def test_use_case_create_company(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns a successful message
        """
        repo = FakeCompanyRepository()
        uc = CreateCompanyUseCase()
        response = uc.create_company(repo, "2400a00k")

        assert response == "Company created"

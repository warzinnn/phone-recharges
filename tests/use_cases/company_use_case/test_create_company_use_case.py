from typing import List

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.application.use_cases.create_company.create_company_use_case import (
    CreateCompanyUseCase,
)
from src.domain.company import Company


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
        uc = CreateCompanyUseCase(repo)
        response = uc.create_company("2400a00k")

        assert response == "Company created"

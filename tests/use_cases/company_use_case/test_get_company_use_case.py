from typing import List

from src.domain.model.company import Company
from src.interfaces.company_repository_interface import CompanyRepositoryInterface
from src.use_cases.get_company.get_company_use_case import GetCompanyUseCase


class FakeCompanyRepository(CompanyRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_company(self) -> List[Company]:
        return [Company("5ca667f8"), Company("472af23a")]

    def select_company_by_id(self, company_id: str) -> List[Company]:
        return [Company("2400a00k")]

    def create_new_company(self, company_id: str) -> Company:
        pass

    def delete_company(self, company_id: str) -> int:
        pass


class TestGetCompanyUseCase:
    def test_use_case_get_company(self):
        """
        GIVEN a use case is proper implemented
        WHEN the use case is required
        THEN check if the implementation returns the companies
        """
        repo = FakeCompanyRepository()
        uc = GetCompanyUseCase()
        response_1 = uc.get_company(repo, "")
        response_2 = uc.get_company(repo, "2400a00k")

        assert len(response_1) > 0
        assert response_1[0]["company_id"] == "5ca667f8"
        assert response_1[1]["company_id"] == "472af23a"
        assert len(response_2) > 0
        assert response_2[0]["company_id"] == "2400a00k"

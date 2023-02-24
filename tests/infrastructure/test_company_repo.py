from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.domain.company import Company
from unittest import mock
import pytest
from src.infrastructure.repository.company_repository import CompanyRepository
import src.infrastructure.entities.orm as ORM

class ConnectionHandlerMock:
    """
    STUB Data
    """
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [
                        mock.call.query(Company)
                    ],
                    [Company('vivo_11')]
                ),
                (
                    [
                        mock.call.query(Company),
                        mock.call.filter(Company.company_id == 'vivo_12')
                    ],
                    [Company('vivo_12')]
                ),
                (
                    [
                        mock.call.query(Company),
                        mock.call.filter(Company.company_id == 'mock_00')
                    ],
                    [] #Empty list to enter in the condition of company_id not in database
                )
            ]
        )
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

@pytest.fixture
def configure_repo():
    """Fixture to return the CompanyRepository with the mock connection"""
    return CompanyRepository(ConnectionHandlerMock)

class TestCompanyRepository:
    def test_select_all_company(self, configure_repo):
        """
        GIVEN a database with companies already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_company()
        assert isinstance(data[0], Company)
        assert data[0].company_id == 'vivo_11'

    def test_select_company_by_id(self, configure_repo):
        """
        GIVEN a database with companies already inserted
        WHEN the select is realized with filter by 'company_id'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_company_by_id('vivo_12')
        assert isinstance(data[0], Company)
        assert data[0].company_id == 'vivo_12'

    def test_create_new_company(self, configure_repo):
        """
        GIVEN a company is created
        WHEN insert the company object into database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.create_new_company('mock_00')
        assert isinstance(data, Company)
        assert data.company_id == 'mock_00'


    def test_delete_company(self, configure_repo):
        """
        GIVEN a company object are in the database
        WHEN delete the company
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)
        """
        data = configure_repo.delete_company('vivo_11')
        assert data == 1
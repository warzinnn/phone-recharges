from typing import List

import pytest

from src.domain.company import Company
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.config.exceptions import EntityAlreadyExists
from src.infrastructure.repository.company_repository import CompanyRepository


@pytest.fixture(scope="class")
def configure_repo():
    """Fixture to return the CompanyRepository with the connection to DB"""
    return CompanyRepository(DBConnectionHandlerPostgre)


@pytest.fixture(scope="class")
def mock_data_for_company():
    """
    Fixture to insert a data into DB.
    After the test is done it will run the 'clean up', which deletes the objects inserted previoulsy
    """
    with DBConnectionHandlerPostgre() as db:
        try:
            company_data_insert = Company("mock_c_11")
            db.session.add(company_data_insert)
            db.session.commit()
            yield
            db.session.delete(company_data_insert)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


@pytest.mark.usefixtures("set_mappers")
class TestCompanyRepository:
    def test_select_all_company(self, configure_repo):
        """
        GIVEN a database with companies already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_company()
        assert isinstance(data[0], Company)

    def test_select_company_by_id(self, configure_repo, mock_data_for_company):
        """
        GIVEN a database with companies already inserted
        WHEN the select is realized with filter by 'company_id'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_company_by_id("mock_c_11")
        assert isinstance(data[0], Company)
        assert data[0].company_id == "mock_c_11"

    def test_select_company_by_id_fail(self, configure_repo, mock_data_for_company):
        """
        GIVEN a database with companies already inserted
        WHEN the select is realized with filter by 'company_id' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_company_by_id("mo")
        assert isinstance(data, List)
        assert data == []

    def test_create_new_company(self, configure_repo):
        """
        GIVEN a company is created
        WHEN insert the company object into database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.create_new_company("mock_company_06")
        assert isinstance(data, Company)
        assert data.company_id == "mock_company_06"

    def test_create_new_company_with_error(self, configure_repo):
        """
        GIVEN a company is already created
        WHEN insert a company object with the same 'company_id' into database
        THEN checks if the error raised is equal to expected
        """
        with pytest.raises(EntityAlreadyExists) as e:
            configure_repo.create_new_company("mock_company_06")
            assert str(e) == "Company already exists."

    def test_delete_company(self, configure_repo):
        """
        GIVEN a company object are in the database
        WHEN delete the company
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)

        Obs: this test deletes the company created in the test 'test_create_new_company'
        """
        data = configure_repo.delete_company("mock_company_06")
        assert data == 1

    def test_delete_company_fail(self, configure_repo):
        """
        GIVEN a company object are in the database
        WHEN delete the company
        THEN checks if the returned value is equal to expected (0 = did not deleted; 1 = was deleted)

        Obs: this test deletes the company created in the test 'test_create_new_company'
        """
        data = configure_repo.delete_company("mock_cccc")
        assert data == 0

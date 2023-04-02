from typing import List

from src.application.interfaces.repository_interfaces.company_repository_interface import (
    CompanyRepositoryInterface,
)
from src.domain.company import Company
from src.infrastructure.config.exceptions import EntityAlreadyExists


class CompanyRepository(CompanyRepositoryInterface):
    """Class to define repository: Company Repository"""

    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_company(self) -> List[Company]:
        """
        Select data in Company table

        Args:
            None
        Returns:
            List[Company]: List with all Companies
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Company).all()
                return data
            except Exception as e:
                return e

    def select_company_by_id(self, company_id: str) -> List[Company]:
        """
        Select data in Company table by company_id

        Args:
            company_id: Id of the company
        Returns:
            List[Company]: List with all Companies matching the id
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Company)
                    .filter(Company.company_id == company_id)
                    .all()
                )
                return data
            except Exception as e:
                return e

    def create_new_company(self, company_id: str) -> Company:
        """
        Insert data in Company table

        Args:
            company_id: Id of the company
        Returns:
            Company: Company object
        Raises:
            EntityAlreadyExists: if Company already exists in database
        """
        with self.__connection_handler() as db:
            try:
                db.session.expire_on_commit = False
                if self.select_company_by_id(company_id):
                    raise EntityAlreadyExists("Company already exists.")
                data_insert = Company(company_id)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as e:
                db.session.rollback()
                raise e

    def delete_company(self, company_id: str) -> int:
        """
        Delete data in Company table by company_id

        Args:
            company_id: Id of the company
        Returns:
            int: represents the status from the deletion (1=ok; 2=nok)
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Company)
                    .filter(Company.company_id == company_id)
                    .delete()
                )
                db.session.commit()
                return data
            except Exception as e:
                return e

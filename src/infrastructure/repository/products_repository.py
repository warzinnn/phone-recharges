from typing import List

from sqlalchemy.exc import IntegrityError

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.domain.products import Products
from src.infrastructure.config.exceptions import (
    DataIsNotPresentInTable,
    EntityAlreadyExists,
)


class ProductsRepository(ProductsRepositoryInterface):
    """Class to define repository: Products Repository"""

    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_products(self) -> List[Products]:
        """
        Select data in Product table

        Args:
            None
        Returns:
            List[Products]: List with all products
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Products).all()
                return data
            except Exception:
                return None

    def select_product_by_id(self, product_id: str) -> List[Products]:
        """
        Select data in Product table by id

        Args:
            id: Id of the product
        Returns:
            List[Products]: List with all products matching the id
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products).filter(Products.id == product_id).all()
                )
                return data
            except Exception:
                return None

    def select_product_by_value(self, value: float) -> List[Products]:
        """
        Select data in Products table by value

        Args:
            value: value of the product
        Returns:
            List[Products]: List with all producties matching the value
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Products).filter(Products.value == value).all()
                return data
            except Exception:
                return None

    def select_products_by_company(self, company_id: str) -> List[Products]:
        """
        Select data in Product table by id_company (foreign key)

        Args:
            id_company: id of the company
        Returns:
            List[Products]: List with all products from the matching id_company
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products)
                    .filter(Products.id_company == company_id)
                    .all()
                )
                return data
            except Exception:
                return None

    def create_new_product(
        self, product_id: str, value: float, company_id: str
    ) -> Products:
        """
        Insert data in Product table

        Args:
            product_id: Id of the product
            value: The value of product
            id_company: id of the company
        Returns:
            Products: Product object
        Raises:
            EntityAlreadyExists: if Product already exists in database
        """
        with self.__connection_handler() as db:
            try:
                # if this flag is set to true it is not possible to return the Product obj (it will be expired)
                db.session.expire_on_commit = False
                if self.select_product_by_id(product_id):
                    raise EntityAlreadyExists("Product already exists.")
                data_insert = Products(product_id, value, company_id)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except IntegrityError:
                db.session.rollback()
                raise DataIsNotPresentInTable("Product does not exists.")
            except Exception as e:
                db.session.rollback()
                raise e

    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        """
        Update value of product in Product table by id_company and product_id

        Args:
            product_id: Id of the product
            value: The value of product
            id_company: id of the company
        Returns:
            int: represents the status from the update (1=ok; 2=nok)
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products)
                    .filter(
                        Products.id_company == id_company, Products.id == product_id
                    )
                    .update({Products.value: value})
                )
                db.session.commit()
                return data
            except Exception as e:
                db.session.rollback()
                raise e

    def delete_product(self, product_id: str) -> int:
        """
        Delete data in Product table by product_id

        Args:
            product_id: Id of the product
        Returns:
            int: represents the status from the deletion (1=ok; 2=nok)
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products)
                    .filter(Products.id == product_id)
                    .delete()
                )
                db.session.commit()
                return data
            except Exception as e:
                db.session.rollback()
                raise e

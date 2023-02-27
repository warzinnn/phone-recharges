from typing import List

from src.domain.model.company import Company
from src.domain.model.products import Products
from src.infrastructure.config.exceptions import EntityAlreadyExists


class ProductsRepository:
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_products(self) -> List[Products]:
        """
        Select data in Product table
        :param - None
        :return - List with all Producties
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Products).all()
                return data
            except Exception:
                return None

    def select_product_by_id(self, product_id: str) -> Products:
        """
        Select data in Product table by id
        :param - id: Id of the product
        :return - List with all producties matching the id
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products).filter(Products.id == product_id).all()
                )
                return data
            except Exception as e:
                return e

    def select_product_by_value(self, value: float) -> Products:
        """
        Select data in Product table by id
        :param - value: value of the product
        :return - List with all producties matching the id
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(Products).filter(Products.value == value).all()
                return data
            except Exception as e:
                return e

    def select_products_by_company(self, company_id: str) -> List[Company]:
        """
        Select data in Product table by id_company (foreign key)
        :param - id_company: id of the company
        :return - List with all producties from the matching id_company
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Products)
                    .filter(Products.id_company == company_id)
                    .all()
                )
                return data
            except Exception as e:
                return e

    def create_new_product(self, product_id: str, value: float, company_id: str) -> Products:
        """
        Insert data in Product table
        :param
            - product_id: Id of the product
            - value: The value of product
            - id_company: id of the company

        :return - Product object

        Explanation
        ===========
        First it will check if the product_id already exists in db and if do not exists, it will create.
        """
        with self.__connection_handler() as db:
            try:
                db.session.expire_on_commit = False # if this flag is set to false it is not possible to return the Product obj (it will be expired)
                if self.select_product_by_id(product_id):
                    raise EntityAlreadyExists("Product already exists.")
                data_insert = Products(product_id, value, company_id)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as e:
                db.session.rollback()
                raise e

    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        """
        Update data in Product table by id_company_value
        :param - id_company: Id of the company
               - value: The value of product
               - company_id: id of the company
        :return - int that represents the status from the update
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
        :param - product_id: Id of the product
        :return - int that represents the status from the deletion
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

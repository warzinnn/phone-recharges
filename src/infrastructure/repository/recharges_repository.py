from typing import List

from sqlalchemy.exc import IntegrityError

from src.domain.model.products import Products
from src.domain.model.recharge import Recharge
from src.infrastructure.config.exceptions import DataIsNotPresentInTable


class RechargeRepository:
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_recharges(self) -> List:
        """
        Select data in Recharges table. (Select with join to also return the Product value and Company id)
        :param - None
        :return - List with all Recharges
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Recharge)
                    .join(Products, Products.id == Recharge.product_id)
                    .with_entities(Recharge, Products.value, Products.id_company)
                    .all()
                )
                return data
            except Exception:
                return None

    def select_all_recharges_by_recharge_id(self, recharge_id: str) -> List:
        """
        Select data in Recharges table. (Select with join to also return the Product value and Company id)
        :param - recharge_id
        :return - List with all Recharges
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Recharge)
                    .filter(Recharge.recharge_id == recharge_id)
                    .join(Products, Products.id == Recharge.product_id)
                    .with_entities(Recharge, Products.value, Products.id_company)
                    .all()
                )
                return data
            except Exception:
                return None

    def select_all_recharges_by_phone_number(self, phone_number: str) -> List:
        """
        Select data in Recharges table. (Select with join to also return the Product value and Company id)
        :param - phone_number
        :return - List with all Recharges
        """
        with self.__connection_handler() as db:
            try:
                data = (
                    db.session.query(Recharge)
                    .filter(Recharge.phone_number == phone_number)
                    .join(Products, Products.id == Recharge.product_id)
                    .with_entities(Recharge, Products.value, Products.id_company)
                    .all()
                )
                return data
            except Exception:
                return None

    def do_recharge(self, phone_number: str, product_id: str) -> Recharge:
        """
        Insert data in Recharges table
        :param
            - phone_number: telephone number
            - product_id: id of product

        :return - Recharge object
        """
        with self.__connection_handler() as db:
            try:
                """if this flag is set to true it is not possible
                to return the Product obj (it will be expired)"""
                db.session.expire_on_commit = False

                data_insert = Recharge(phone_number, product_id)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except IntegrityError:
                db.session.rollback()
                raise DataIsNotPresentInTable("Product does not exists.")
            except Exception as e:
                db.session.rollback()
                raise e

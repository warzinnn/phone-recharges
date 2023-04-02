from typing import List

import pytest

from src.domain.recharge import Recharge
from src.infrastructure.config.connection_postgres import DBConnectionHandlerPostgre
from src.infrastructure.config.exceptions import DataIsNotPresentInTable
from src.infrastructure.repository.recharges_repository import RechargeRepository


@pytest.fixture(scope="class")
def configure_repo():
    """Fixture to return the RechargeRepository with the connection to DB"""
    return RechargeRepository(DBConnectionHandlerPostgre)


@pytest.fixture()
def clean_recharge():
    """Fixture to clean database after the insert in the test of 'do_recharge'"""
    yield
    with DBConnectionHandlerPostgre() as db:
        db.session.query(Recharge).filter(
            Recharge.phone_number == "5511982827373"
        ).delete()
        db.session.commit()


@pytest.mark.usefixtures("set_mappers")
class TestRechagesRepository:
    def test_select_all_recharges(self, configure_repo):
        """
        GIVEN a database with recharges already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_recharges()
        assert isinstance(data[0][0], Recharge)
        assert isinstance(data[0][1], float)
        assert isinstance(data[0][2], str)

    def test_select_all_recharges_by_recharge_id(self, configure_repo):
        """
        GIVEN a database with recharges already inserted
        WHEN the select is realized with filter by 'recharge_id'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_recharges_by_recharge_id(
            "0be28cc4-7776-4339-9d02-325fae1b6084"
        )
        assert isinstance(data[0][0], Recharge)
        assert isinstance(data[0][1], float)
        assert isinstance(data[0][2], str)

    def test_select_all_recharges_by_recharge_id_fail(self, configure_repo):
        """
        GIVEN a database with recharges already inserted
        WHEN the select is realized with filter by 'phone_number' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_recharges_by_recharge_id("0be28cc4-")
        assert isinstance(data, List)
        assert data == []

    def test_select_all_recharges_by_phone_number(self, configure_repo):
        """
        GIVEN a database with recharges already inserted
        WHEN the select is realized with filter by 'phone_number'
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_recharges_by_phone_number("5511999999999")
        assert isinstance(data[0][0], Recharge)
        assert isinstance(data[0][1], float)
        assert isinstance(data[0][2], str)

    def test_select_all_recharges_by_phone_number_fail(self, configure_repo):
        """
        GIVEN a database with recharges already inserted
        WHEN the select is realized with filter by 'phone_number' with invalid input
        THEN checks if the returned object is equal to expected
        """
        data = configure_repo.select_all_recharges_by_phone_number("5511")
        assert isinstance(data, List)
        assert data == []

    def test_do_recharge(self, configure_repo, clean_recharge):
        """
        GIVEN a recharge is created
        WHEN insert the recharge object into database
        THEN checks if the returned object from insert is equal to expected
        """
        data = configure_repo.do_recharge("5511982827373", "claro_50")
        assert isinstance(data, Recharge)

    def test_do_recharge_fail_invalid_product(self, configure_repo):
        """
        GIVEN a recharge is created with invalid product_id
        WHEN insert the recharge object into database
        THEN checks if the error raised is equal to expected
        """
        with pytest.raises(DataIsNotPresentInTable) as e:
            configure_repo.do_recharge("5511982827373", "xx")
            assert str(e) == "Product does not exists."

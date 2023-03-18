from datetime import datetime
from uuid import UUID

import pytest

from src.domain.model.recharge import Recharge


@pytest.fixture
def mock_recharge() -> Recharge:
    """Fixture to return a Recharge object"""
    return Recharge("5511999999999", "claro_50")


class TestRecharge:
    def test_recharges_object_attributes_are_the_expected_type(self, mock_recharge):
        """
        GIVEN a recharge object is created
        WHEN attributes are required
        THEN checks if the type of attributes is equal to the expected data
        """
        assert isinstance(mock_recharge.recharge_id, UUID)
        assert isinstance(mock_recharge.created_at, datetime)
        assert isinstance(mock_recharge.phone_number, str)
        assert isinstance(mock_recharge.product_id, str)

    def test_recharges_object_attributes_is_equal_to_expected(self, mock_recharge):
        """
        GIVEN a recharge object is created
        WHEN attribute phone_number and product_id is requeried
        THEN checks if the attributes is equal to the expected data
        """
        assert mock_recharge.phone_number == "5511999999999"
        assert mock_recharge.product_id == "claro_50"

    def test_recharge_obj_as_dict(self, mock_recharge):
        """
        GIVEN a recharge object is created
        WHEN converts the recharge object to dictionary
        THEN checks if the method 'as_dict()' is returning the expected dictionary
        """
        expected_dict = {
            "recharge_id": mock_recharge.recharge_id.__str__(),
            "created_at": mock_recharge.created_at.__str__(),
            "phone_number": "5511999999999",
            "product_id": "claro_50",
        }

        assert mock_recharge.as_dict() == expected_dict

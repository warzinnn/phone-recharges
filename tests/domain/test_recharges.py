from uuid import UUID
from src.domain.model.recharge import Recharge
from uuid import UUID
from datetime import datetime

class TestRecharge():
    def test_recharges_object_attributes_is_the_expected_type(self):
        """
        GIVEN a recharge object is created
        WHEN attributes are required
        THEN checks if the type of attributes is equal to the expected data
        """
        new_recharge = Recharge('5511999999999', 'claro_50')
        
        assert isinstance(new_recharge.recharge_id, UUID)
        assert isinstance(new_recharge.created_at, datetime)
        assert isinstance(new_recharge.phone_number, str)
        assert isinstance(new_recharge.product_id, str)

    def test_recharges_object_attributes_is_equal_to_expected(self):
        """
        GIVEN a recharge object is created
        WHEN attribute phone_number and product_id is requeried
        THEN checks if the attributes is equal to the expected data
        """
        new_recharge = Recharge('5511999999999', 'claro_50')
        
        assert new_recharge.phone_number == '5511999999999'
        assert new_recharge.product_id == 'claro_50'

    def test_recharge_obj_as_dict(self):
        """
        GIVEN a recharge object is created
        WHEN converts the recharge object to dictionary
        THEN checks if the method 'as_dict()' is returning the expected dictionary
        """
        new_recharge = Recharge('5511999999999', 'claro_50')

        expected_dict = {"recharge_id": new_recharge.recharge_id.__str__(), "created_at": new_recharge.created_at.__str__(), "phone_number": "5511999999999", "product_id": "claro_50"}

        assert new_recharge.as_dict() == expected_dict
   
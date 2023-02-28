import json

from src.domain.model.company import Company


class TestCompany:
    def test_company_object_attributes_is_the_expected_type(self):
        """
        GIVEN a company object is created
        WHEN attributes are required
        THEN checks if the type of attributes is equal to the expected data
        """
        new_company = Company("claro_11")
        assert isinstance(new_company.company_id, str)
      

    def test_company_attributes_equal_to_expected(self):
        """
        GIVEN a company object is created
        WHEN attribute company_id is requeried
        THEN checks if attribute company_id from the company object is equal to the expected data
        """
        new_company = Company("claro_11")
        assert new_company.company_id == "claro_11"

    def test_company_obj_as_dict(self):
        """
        GIVEN a company object is created
        WHEN converts the company object into dictionary
        THEN returns the user object as a dictionary with keys company_id, products, product.id and product.value
        """
        expected_dict = {"company_id": "claro_11"}
        new_company = Company("claro_11")

        assert new_company.company_as_dict() == expected_dict

    def test_company_dict_serialized_as_JSON(self):
        """
        GIVEN a company object is created
        WHEN converts the company object into dictionary
        THEN checks if the returned dict serialized in json is equal to the expected json
        """
        new_company = Company("claro_11")
        expected_json = """{"company_id": "claro_11"}"""
        assert json.dumps(new_company.company_as_dict()) == expected_json

import json

from src.domain.products import Products


class TestProducts:
    def test_products_attributes_equal_to_expected(self):
        """
        GIVEN a product object is created
        WHEN attributes id and value are queried
        THEN checks if attributes id and value from product object is equal to the expected data
        """
        new_product = Products("claro_10", 10)

        assert new_product.id == "claro_10"
        assert new_product.value == 10

    def test_products_obj_as_dict(self):
        """
        GIVEN a product object is created
        WHEN converts the product object into dictionary
        THEN returns the product object as a dictionary with keys id and value
        """
        expected_dict = {
            "company_id": "claro_11",
            "products": [{"id": "claro_10", "value": 10.0}],
        }
        new_product = Products("claro_10", 10.0, "claro_11")

        assert new_product.product_as_dict() == expected_dict

    def test_products_dict_serialized_as_JSON(self):
        """
        GIVEN a product object is created
        WHEN converts the product object into dictionary
        THEN checks if the returned dict serialized in json is equal to the expected json
        """
        new_product = Products("claro_10", 10.0, "claro_11")
        expected_json = """{"company_id": "claro_11", "products": [{"id": "claro_10", "value": 10.0}]}"""
        assert json.dumps(new_product.product_as_dict()) == expected_json

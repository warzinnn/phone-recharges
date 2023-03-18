import pytest

from src.domain.model.products import Products


@pytest.fixture
def mock_product() -> Products:
    """Fixture to return a Product object"""
    return Products("claro_10", 10.0, "claro_11")


class TestProducts:
    def test_products_object_attributes_are_the_expected_type(self, mock_product):
        """
        GIVEN a product object is created
        WHEN attributes are required
        THEN checks if the type of attributes is equal to the expected data
        """
        assert isinstance(mock_product.id, str)
        assert isinstance(mock_product.value, float)
        assert isinstance(mock_product.id_company, str)

    def test_products_attributes_equal_to_expected(self, mock_product):
        """
        GIVEN a product object is created
        WHEN attributes id and value are queried
        THEN checks if attributes id and value from product object is equal to the expected data
        """
        assert mock_product.id == "claro_10"
        assert mock_product.value == 10
        assert mock_product.id_company == "claro_11"

    def test_products_obj_as_dict(self, mock_product):
        """
        GIVEN a product object is created
        WHEN converts the product object into dictionary
        THEN returns the product object as a dictionary with keys id and value
        """
        expected_dict = {
            "company_id": "claro_11",
            "products": [{"id": "claro_10", "value": 10.0}],
        }
        assert mock_product.product_as_dict() == expected_dict

    def test_product_object_comparison(self, mock_product):
        """
        GIVEN a product object is created
        WHEN compare instances of product object
        THEN checks if the comparison work as expected
        """
        product_test1 = mock_product
        product_test2 = mock_product

        assert product_test2 == product_test1

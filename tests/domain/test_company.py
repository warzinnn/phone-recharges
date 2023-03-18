import pytest

from src.domain.model.company import Company


@pytest.fixture
def mock_company() -> Company:
    """Fixture to return a company object"""
    return Company("claro_11")


class TestCompany:
    def test_company_object_attributes_is_the_expected_type(self, mock_company):
        """
        GIVEN a company object is created
        WHEN attributes are required
        THEN checks if the type of attributes is equal to the expected data
        """
        assert isinstance(mock_company.company_id, str)

    def test_company_attributes_equal_to_expected(self, mock_company):
        """
        GIVEN a company object is created
        WHEN attribute company_id is requeried
        THEN checks if attribute company_id from the company object is equal to the expected data
        """
        assert mock_company.company_id == "claro_11"

    def test_company_obj_as_dict(self, mock_company):
        """
        GIVEN a company object is created
        WHEN converts the company object into dictionary
        THEN returns the user object as a dictionary with keys company_id, products, product.id and product.value
        """
        expected_dict = {"company_id": "claro_11"}
        assert mock_company.company_as_dict() == expected_dict

    def test_company_object_comparison(self, mock_company):
        """
        GIVEN a company object is created
        WHEN compare instances of company object
        THEN checks if the comparison work as expected
        """
        company_test1 = mock_company
        company_test2 = mock_company

        assert company_test2 == company_test1

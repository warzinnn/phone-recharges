from typing import Dict


class TestBlueprintProduct:
    def test_blueprint_products_status_code_equals_200(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/company/products' is requested with GET method
        THEN checks if http status code is equal to 200
        """
        response = client.get("/company/products")
        assert response.status_code == 200

    def test_blueprint_products_with_wrong_http_method(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN '/company/products' is requested with wrong HTTP Method
        THEN checks if http status code is equal to 405
        """
        response = client.patch("/company/products")
        assert response.status_code == 405

    def test_blueprint_products_content_type_match_json(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN '/company/products' is requested
        THEN checks if http header content-type code is equal to application/json
        """
        response = client.get("/company/products")
        assert response.headers["Content-Type"] == "application/json"

    def test_blueprint_products_response_equals_to_list_type(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/company/products' is requested
        THEN checks if the output is equal to a list type
        """
        response = client.get("/company/products")
        assert isinstance(response.json, Dict)

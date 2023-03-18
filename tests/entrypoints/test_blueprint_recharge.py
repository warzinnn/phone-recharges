from typing import List


class TestBlueprintRecharge:
    def test_blueprint_recharge_status_code_equals_200(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/recharge' is requested with GET method
        THEN checks if http status code is equal to 200
        """
        response = client.get("/recharge/")
        assert response.status_code == 200

    def test_blueprint_products_with_wrong_http_method(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/recharge' is requested with wrong HTTP Method
        THEN checks if http status code is equal to 405
        """
        response = client.patch("/recharge/")
        assert response.status_code == 405

    def test_blueprint_products_content_type_match_json(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint'/recharge' is requested with GET method
        THEN checks if http header content-type code is equal to application/json
        """
        response = client.get("/recharge/")
        assert response.headers["Content-Type"] == "application/json"

    def test_blueprint_products_response_equals_to_list_type(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/recharge' is requested
        THEN checks if the output is equal to a list type
        """
        response = client.get("/recharge/")
        assert isinstance(response.json, List)

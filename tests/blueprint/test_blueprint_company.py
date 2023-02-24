from typing import List


class TestBlueprintCompany():

    def test_blueprint_company_status_code_equals_200(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/company' is requested with GET method
        THEN checks if http status code is equal to 200
        """
        response = client.get("/company/")
        assert response.status_code == 200

    def test_blueprint_company_with_wrong_http_method(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint with date param '/company'  is requested with wrong HTTP Method
        THEN checks if http status code is equal to 405
        """
        response = client.put("/company/")
        assert response.status_code == 405

    def test_blueprint_company_content_type_match_json(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint with date param '/company' is requested (GET)
        THEN checks if http header content-type code is equal to application/json
        """
        response = client.get("/company/")
        assert response.headers["Content-Type"] == "application/json"

    def test_blueprint_company_response_equals_to_list_type(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint with date param '/company'
        THEN checks if the output is equal to a list type
        """
        response = client.get("/company/")
        assert isinstance(response.json, List)
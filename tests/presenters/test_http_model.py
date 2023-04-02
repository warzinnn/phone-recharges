from src.application.presenters.http_model import HttpResponseModel


class TestHttpResponseModel:
    def test_http_response_model_object_instanciation(self):
        """
        GIVEN a http response model object is created
        WHEN the object is instantiated
        THEN checks if the attributes are equal to the expected data
        """
        model = HttpResponseModel(
            message="Succeed", data=[{"info": "1"}], status_code=200
        )
        assert model.message == "Succeed"
        assert model.data == [{"info": "1"}]
        assert model.status_code == 200

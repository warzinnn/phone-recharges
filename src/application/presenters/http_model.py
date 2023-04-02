class HttpRequestModel:
    """Class to define the representation of http request"""

    pass


class HttpResponseModel:
    """Class to define the representation of http response"""

    def __init__(self, message: str, data: any, status_code: int) -> None:
        self.message = message
        self.data = data
        self.status_code = status_code

    def as_dict(self):
        return {"message": self.message, "data": self.data}

    def __repr__(self):
        return f"HttpResponseModel(message={self.message}, data={self.data})"

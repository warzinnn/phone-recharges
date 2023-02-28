class Products:
    def __init__(self, id: str, value: float, id_company: str) -> None:
        self.id = id
        self.value = value
        self.id_company = id_company

    def __repr__(self) -> str:
        return f"Products(id={self.id}, value={self.value})"

    def product_as_dict(self) -> dict:
        return {
            "company_id": self.id_company,
            "products": [{"id": self.id, "value": self.value}],
        }

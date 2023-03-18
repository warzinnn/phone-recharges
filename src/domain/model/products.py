class Products:
    def __init__(self, id: str, value: float, id_company: str) -> None:
        self.id = id
        self.value = value
        self.id_company = id_company

    def __repr__(self) -> str:
        return (
            f"Products(id={self.id}, value={self.value}, company_id={self.id_company})"
        )

    def product_as_dict(self) -> dict:
        """Return object in dict form"""
        return {
            "company_id": self.id_company,
            "products": [{"id": self.id, "value": self.value}],
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, Products):
            if (
                other.id == self.id
                and other.value == self.value
                and other.id_company == self.id_company
            ):
                return True
        return False

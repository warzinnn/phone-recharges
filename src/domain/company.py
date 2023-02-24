class Company:
    def __init__(self, company_id:str) -> None:
        self.company_id = company_id

    def company_as_dict(self) -> dict:
        return {"company_id": self.company_id}

    def __repr__(self) -> str:
        return f'Company(company_id={self.company_id})'

    
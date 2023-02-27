import uuid
import datetime

class Recharge:
    def __init__(self, phone_number: str, product_id: str) -> None:
        self.recharge_id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.phone_number = phone_number
        self.product_id = product_id

    def __repr__(self) -> str:
        return f"Recharge(id_recharge={self.recharge_id}, created_at={self.created_at}, phone_number={self.phone_number}, id_product={self.product_id})"

    def as_dict(self):
        return {"recharge_id": self.recharge_id.__str__(), "created_at":self.created_at.__str__(), "phone_number": self.phone_number, "product_id": self.product_id}



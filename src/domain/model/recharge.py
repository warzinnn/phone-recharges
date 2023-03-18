import datetime
import uuid


class Recharge:
    def __init__(self, phone_number: str, product_id: str) -> None:
        self.recharge_id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.phone_number = phone_number
        self.product_id = product_id

    def __repr__(self) -> str:
        return f"Recharge(id_recharge={self.recharge_id}, created_at={self.created_at},\
        phone_number={self.phone_number}, id_product={self.product_id})"

    def as_dict(self) -> dict:
        """Return object in dict form"""
        return {
            "recharge_id": self.recharge_id.__str__(),
            "created_at": self.created_at.__str__(),
            "phone_number": self.phone_number,
            "product_id": self.product_id,
        }

    def __eq__(self, other) -> bool:
        if isinstance(other, Recharge):
            if (
                other.recharge_id == self.recharge_id
                and other.created_at == self.created_at
                and other.phone_number == self.phone_number
                and other.product_id == self.product_id
            ):
                return True
        return False

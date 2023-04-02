from abc import ABC, abstractmethod
from typing import List

from src.domain.company import Company
from src.domain.products import Products


class ProductsRepositoryInterface(ABC):
    @abstractmethod
    def select_all_products(self) -> List[Products]:
        raise NotImplementedError

    @abstractmethod
    def select_product_by_id(self, product_id: str) -> Products:
        raise NotImplementedError

    @abstractmethod
    def select_product_by_value(self, value: float) -> Products:
        raise NotImplementedError

    @abstractmethod
    def select_products_by_company(self, company_id: str) -> List[Company]:
        raise NotImplementedError

    @abstractmethod
    def create_new_product(
        self, product_id: str, value: float, company_id: str
    ) -> Products:
        raise NotImplementedError

    @abstractmethod
    def update_product(self, id_company: str, product_id: str, value: float) -> int:
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, product_id: str) -> int:
        raise NotImplementedError

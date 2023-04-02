from abc import ABC, abstractmethod
from typing import List

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.domain.products import Products


class GetProductsUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_products(self, company_id: str) -> List[Products]:
        raise NotImplementedError

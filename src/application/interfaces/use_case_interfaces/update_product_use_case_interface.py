from abc import ABC, abstractmethod

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)


class UpdateProductsUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_product(
        self, company_id: str, product_id: str, product_value: float
    ) -> str:
        raise NotImplementedError

from abc import ABC, abstractmethod

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)


class DeleteProductUseCaseInterface(ABC):
    @abstractmethod
    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, product_id: str) -> str:
        raise NotImplementedError

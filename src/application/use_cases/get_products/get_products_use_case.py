from typing import List

from src.application.interfaces.repository_interfaces.products_repository_interface import (
    ProductsRepositoryInterface,
)
from src.application.interfaces.use_case_interfaces.get_products_use_case_interface import (
    GetProductsUseCaseInterface,
)
from src.domain.products import Products


class GetProductsUseCase(GetProductsUseCaseInterface):
    """Class to define use_case: Get Products"""

    def __init__(self, repository: ProductsRepositoryInterface) -> None:
        self.repository = repository

    def get_products(self, company_id: str) -> List[Products]:
        """Get Products Use Case

        Args:
            company_id: company id
        Returns:
            List[Products]: List with products
        """
        if company_id:
            data = self.repository.select_products_by_company(company_id)
        else:
            data = self.repository.select_all_products()

        data_as_dict = [i.product_as_dict() for i in data]

        """
        group products by company_id. (if company_id matches then agroup the products in the same dict key)
        after that removes the entry marked as None and then returns the data
        """
        for i in range(len(data_as_dict)):
            for j in range(i + 1, len(data_as_dict)):
                if (
                    data_as_dict[i]["company_id"] == data_as_dict[j]["company_id"]
                    and data_as_dict[j]["products"] is not None
                ):
                    data_as_dict[i]["products"].append(data_as_dict[j]["products"][0])
                    data_as_dict[j]["products"] = None

        for entry in data_as_dict[:]:
            if entry["products"] is None:
                data_as_dict.remove(entry)

        return data_as_dict

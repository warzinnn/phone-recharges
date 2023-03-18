import itertools
import re
from typing import List

from src.domain.model.products import Products
from src.interfaces.products_repository_interface import ProductsRepositoryInterface
from src.use_cases.exceptions import DataValidationError


class GetProductsUseCase:
    """Class to define use_case: Get Products"""

    def get_products(
        self, repo: ProductsRepositoryInterface, company_id: str
    ) -> List[Products]:
        """Get Products Use Case

        Args:
            repo: Products Repository Interface
            company_id: company id
        Returns:
            List[Products]: List with products

        Explanation
        ===========
        Combinations(): This iterator prints all the possible combinations(without replacement)\
         of the container passed in arguments in the specified group size in sorted order.
        - It will compare the elements of array between them. If the company_id of elements match,\
        them it will agroup the product.id and product value in the same array, and remove the spare element.
        """
        if company_id:
            company_id = self.validate_company_id(company_id)
            data = repo.select_products_by_company(company_id)
        else:
            data = repo.select_all_products()

        data_as_dict = [i.product_as_dict() for i in data]
        for x, y in itertools.combinations(data_as_dict, 2):
            if x in data_as_dict and y in data_as_dict:
                if x["company_id"] == y["company_id"]:
                    x["products"].append(y["products"][0])
                    data_as_dict.remove(y)
        return data_as_dict

    def validate_company_id(self, company_id: str):
        """
        Auxiliar method to validate the company_id provided by the user
        Regex:
            matches any non-word character.
        """
        regex_str = r"\W"
        input = re.search(regex_str, company_id)

        if input is None:
            if len(company_id) > 20:
                raise DataValidationError("Invalid company_id")
            else:
                return company_id
        else:
            raise DataValidationError("Invalid company_id")

from flask import Blueprint, jsonify, request

from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.config.exceptions import EntityAlreadyExists
from src.infrastructure.repository.products_repository import ProductsRepository
from src.use_cases.create_product.create_product_use_case import CreateProductUseCase
from src.use_cases.delete_product.delete_product_use_case import DeleteProductUseCase
from src.use_cases.get_products.get_products_use_case import GetProductsUseCase
from src.use_cases.update_product.update_product_use_case import UpdateProductUseCase

blueprint_products = Blueprint(name="blueprint_products", import_name=__name__)


@blueprint_products.route("/products", methods=["GET"])
def get_products():
    try:
        uc = GetProductsUseCase()
        repo = ProductsRepository(DBConnectionHandler)

        query_param_company_id = request.args.get("company_id")

        response = uc.get_products(repo, query_param_company_id)
        return response
    except Exception:
        return jsonify({"message": "Error"})


@blueprint_products.route("/products", methods=["POST"])
def create_product():
    try:
        uc = CreateProductUseCase()
        repo = ProductsRepository(DBConnectionHandler)

        json_input = request.json
        param_company_id = None
        param_product_id = None
        param_product_value = None

        # READ INPUT FROM JSON PAYLOAD
        param_company_id = json_input["company_id"]
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        else:
                            param_product_value = v
                    data = uc.create_product(
                        repo, param_company_id, param_product_id, param_product_value
                    )
        return jsonify({"message": data})
    except EntityAlreadyExists as e:
        return jsonify({"message": str(e)})
    except Exception:
        return jsonify({"message": "Error"})


@blueprint_products.route("/products", methods=["PUT"])
def update_product():
    try:
        uc = UpdateProductUseCase()
        repo = ProductsRepository(DBConnectionHandler)

        json_input = request.json
        param_company_id = None
        param_product_id = None
        param_product_value = None

        # READ INPUT FROM JSON PAYLOAD
        param_company_id = json_input["company_id"]
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        else:
                            param_product_value = v
                    data = uc.update_product(
                        repo, param_company_id, param_product_id, param_product_value
                    )
        return jsonify({"message": data})
    except Exception as e:
        return jsonify({"message": str(e)})


@blueprint_products.route("/products", methods=["DELETE"])
def delete_product():
    try:
        uc = DeleteProductUseCase()
        repo = ProductsRepository(DBConnectionHandler)

        query_param_product_id = request.args.get("product_id")

        data = uc.delete_product(repo, query_param_product_id)
        return jsonify({"message": data})
    except Exception:
        return jsonify({"message": "Error"})

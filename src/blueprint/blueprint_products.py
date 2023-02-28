import itertools

from flask import Blueprint, jsonify, request

from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.config.exceptions import EntityAlreadyExists
from src.infrastructure.repository.products_repository import \
    ProductsRepository

blueprint_products = Blueprint(name="blueprint_products", import_name=__name__)


@blueprint_products.route("/products", methods=["GET"])
def get_products():
    repo = ProductsRepository(DBConnectionHandler)

    query_param_company_id = request.args.get("company_id")

    try:
        if query_param_company_id:
            data = repo.select_products_by_company(query_param_company_id)
        else:
            data = repo.select_all_products()

        data_as_dict = [i.product_as_dict() for i in data]
        for x, y in itertools.combinations(data_as_dict, 2):
            if x in data_as_dict and y in data_as_dict:
                if x["company_id"] == y["company_id"]:
                    x["products"].append(y["products"][0])
                    data_as_dict.remove(y)
        return data_as_dict
    except Exception:
        return jsonify({"message": "error"})


@blueprint_products.route("/products", methods=["POST"])
def create_product():
    repo = ProductsRepository(DBConnectionHandler)

    json_input = request.json
    param_company_id = None
    param_product_id = None
    param_product_value = None

    # READ INPUT FROM JSON PAYLOAD
    try:
        param_company_id = json_input["company_id"]
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        else:
                            param_product_value = v
                    data = repo.create_new_product(
                        param_product_id, param_product_value, param_company_id
                    )
        return jsonify({"message": "created"})
    except EntityAlreadyExists as e:
        return jsonify({"message": str(e)})
    except Exception:
        return jsonify({"message": "error"})


@blueprint_products.route("/products", methods=["PUT"])
def update_product():
    repo = ProductsRepository(DBConnectionHandler)

    json_input = request.json
    param_company_id = None
    param_product_id = None
    param_product_value = None

    # READ INPUT FROM JSON PAYLOAD
    try:
        param_company_id = json_input["company_id"]
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        else:
                            param_product_value = v
                    data = repo.update_product(
                        param_company_id, param_product_id, param_product_value
                    )
        return jsonify({"message": data})
    except Exception:
        return jsonify({"message": "error"})


@blueprint_products.route("/products", methods=["DELETE"])
def delete_product():
    repo = ProductsRepository(DBConnectionHandler)
    query_param_product_id = request.args.get("product_id")

    try:
        data = repo.delete_product(query_param_product_id)
        return jsonify({"message": data})
    except Exception:
        return jsonify({"message": "error"})

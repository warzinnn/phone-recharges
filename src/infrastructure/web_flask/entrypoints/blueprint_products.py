from flask import Blueprint, jsonify, request

from src.application.presenters.http_model import HttpResponseModel
from src.infrastructure.composite.create_product_composite import (
    create_product_composite,
)
from src.infrastructure.composite.delete_product_composite import (
    delete_product_composite,
)
from src.infrastructure.composite.get_products_composite import get_products_composite
from src.infrastructure.composite.update_product_composite import (
    update_product_composite,
)

# Defining blueprint
blueprint_products = Blueprint(name="blueprint_products", import_name=__name__)


@blueprint_products.route("/products", methods=["GET"])
def get_products():
    try:
        # Get query_parameter
        query_param_company_id = request.args.get("company_id")

        # Use composite to instantiate controller
        controller = get_products_composite()
        response = controller.handle(company_id=query_param_company_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_products.route("/products", methods=["POST"])
def create_product():
    try:
        # Use composite to instantiate controller
        controller = create_product_composite()

        # Get parameters from payload
        json_input = request.json
        param_company_id = json_input["company_id"]
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        else:
                            param_product_value = v
                    response = controller.handle(
                        company_id=param_company_id,
                        product_id=param_product_id,
                        product_value=param_product_value,
                    )
                    if response.message == "Failed":
                        return jsonify(response.as_dict()), response.status_code

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_products.route("/products", methods=["PUT"])
def update_product():
    try:
        # Use composite to instantiate controller
        controller = update_product_composite()

        # Get parameters from payload
        json_input = request.json
        param_company_id = json_input["company_id"]
        param_product_id = None
        param_product_value = None
        for key, value in json_input.items():
            if key == "products":
                for i in value:
                    for k, v in i.items():
                        if k == "id":
                            param_product_id = v
                        elif k == "value":
                            param_product_value = v
                    response = controller.handle(
                        company_id=param_company_id,
                        product_id=param_product_id,
                        product_value=param_product_value,
                    )
                    if response.message == "Failed":
                        return jsonify(response.as_dict()), response.status_code

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_products.route("/products", methods=["DELETE"])
def delete_product():
    try:
        # Get query_parameter
        query_param_product_id = request.args.get("product_id")

        # Use composite to instantiate controller
        controller = delete_product_composite()
        response = controller.handle(product_id=query_param_product_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code

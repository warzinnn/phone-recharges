from flask import Blueprint, jsonify, request

from src.application.presenters.http_model import HttpResponseModel
from src.infrastructure.composite.create_company_composite import (
    create_company_composite,
)
from src.infrastructure.composite.delete_company_composite import (
    delete_company_composite,
)
from src.infrastructure.composite.get_company_composite import get_company_composite

from .blueprint_products import blueprint_products

# Defining blueprint
blueprint_company = Blueprint(name="blueprint_company", import_name=__name__)

# Nested blueprint register to access the URI: /company/products
blueprint_company.register_blueprint(blueprint_products)


@blueprint_company.route("/", methods=["GET"])
def get_company():
    try:
        # Get query_parameter
        query_param_company_id = request.args.get("company_id")

        # Use composite to instantiate controller
        controller = get_company_composite()
        response = controller.handle(company_id=query_param_company_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_company.route("/", methods=["POST"])
def create_company():
    try:
        # Get parameter from payload
        json_input = request.json
        param_company_id = json_input["company_id"]

        # Use composite to instantiate controller
        controller = create_company_composite()
        response = controller.handle(company_id=param_company_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_company.route("/", methods=["DELETE"])
def delete_company():
    try:
        # Get query_parameter
        query_param_company_id = request.args.get("company_id")

        # Use composite to instantiate controller
        controller = delete_company_composite()
        response = controller.handle(company_id=query_param_company_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code

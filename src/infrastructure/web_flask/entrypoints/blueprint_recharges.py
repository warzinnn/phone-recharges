from flask import Blueprint, jsonify, request

from src.application.presenters.http_model import HttpResponseModel
from src.infrastructure.composite.do_recharge_composite import do_recharge_composite
from src.infrastructure.composite.get_recharges_composite import get_recharges_composite

# Defining blueprint
blueprint_recharges = Blueprint(name="blueprint_recharges", import_name=__name__)


@blueprint_recharges.route("/", methods=["GET"])
def get_recharges():
    try:
        # Get query_parameter
        query_param_id = request.args.get("recharge_id")
        query_param_phone_number = request.args.get("phone_number")

        # Use composite to instantiate controller
        controller = get_recharges_composite()
        response = controller.handle(
            recharge_id=query_param_id, phone_number=query_param_phone_number
        )

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code


@blueprint_recharges.route("/", methods=["POST"])
def do_recharge():
    try:
        # Get parameters from payload
        json_input = request.json
        param_phone_number = json_input["phone_number"]
        param_product_id = json_input["product_id"]

        # Use composite to instantiate controller
        controller = do_recharge_composite()
        response = controller.handle(param_phone_number, param_product_id)

        # return response as json
        return jsonify(response.as_dict()), response.status_code
    except Exception:
        response = HttpResponseModel("Failed", "Generic Error", 400)
        return jsonify(response.as_dict()), response.status_code

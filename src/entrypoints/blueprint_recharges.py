from flask import Blueprint, jsonify, request

from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.repository.recharges_repository import RechargeRepository
from src.use_cases.do_recharge.do_recharge_use_case import DoRechargeUseCase
from src.use_cases.get_recharges.get_recharges_use_case import GetRechargesUseCase

blueprint_recharges = Blueprint(name="blueprint_recharges", import_name=__name__)


@blueprint_recharges.route("/", methods=["GET"])
def get_recharges():
    try:
        uc = GetRechargesUseCase()
        repo = RechargeRepository(DBConnectionHandler)

        query_param_id = request.args.get("recharge_id")
        query_param_phone_number = request.args.get("phone_number")

        data = uc.get_recharges(repo, query_param_id, query_param_phone_number)
        return data
    except Exception as e:
        return jsonify({"message": str(e)})


@blueprint_recharges.route("/", methods=["POST"])
def do_recharge():
    try:
        uc = DoRechargeUseCase()
        repo = RechargeRepository(DBConnectionHandler)

        json_input = request.json
        param_phone_number = json_input["phone_number"]
        param_product_id = json_input["product_id"]

        data = uc.do_recharge(repo, param_phone_number, param_product_id)
        return jsonify({"recharge_id": data.recharge_id, "created_at": data.created_at})
    except Exception:
        return jsonify({"message": "Error"})

from flask import Blueprint, request, jsonify
from src.infrastructure.repository.recharges_repository import RechargeRepository
from src.infrastructure.config.connection import DBConnectionHandler


blueprint_recharges = Blueprint(name="blueprint_recharges", import_name=__name__)


@blueprint_recharges.route("/", methods=["GET"])
def get_recharges():
    query_param_id = request.args.get('recharge_id')
    query_param_phone_number = request.args.get('phone_number')

    repo = RechargeRepository(DBConnectionHandler)

    try:
        response = []
        data = None
        if query_param_id:
            data = repo.select_all_recharges_by_recharge_id(query_param_id)
        elif query_param_phone_number:
            data = repo.select_all_recharges_by_phone_number(query_param_phone_number)
        else:
            data = repo.select_all_recharges()

        for entry in data:
            tmp_dict = entry[0].as_dict()
            tmp_dict["company_id"] = entry[2]
            tmp_dict["value"] = entry[1]
            response.append(tmp_dict)

        return response
    except Exception:
        return jsonify({"message": "error"})


@blueprint_recharges.route("/", methods=["POST"])
def do_recharge():
    repo = RechargeRepository(DBConnectionHandler)
    json_input = request.json
    param_phone_number = json_input['phone_number']
    param_product_id = json_input['product_id']

    try:
        data = repo.do_recharge(param_phone_number, param_product_id)
        return jsonify({'recharge_id': data.recharge_id, "created_at": data.created_at})
    except Exception:
        return jsonify({"message": "error"})
    


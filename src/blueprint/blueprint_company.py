from flask import Blueprint, jsonify, request
from src.infrastructure.repository.company_repository import CompanyRepository
from src.infrastructure.config.connection import DBConnectionHandler
from .blueprint_products import blueprint_products
from src.infrastructure.config.exceptions import EntityAlreadyExists


# Defining blueprint
blueprint_company = Blueprint(name='blueprint_company', import_name=__name__)

# Nested blueprint register to access the URI: /company/products
blueprint_company.register_blueprint(blueprint_products)


@blueprint_company.route("/", methods=["GET"])
def get_company():
    repo = CompanyRepository(DBConnectionHandler)

    query_param_company_id = request.args.get('company_id')

    try:
        if query_param_company_id:
            data = repo.select_company_by_id(query_param_company_id)
        else:
            data = repo.select_all_company()

        response = [i.company_as_dict() for i in data]
        return response
    except Exception:
        return jsonify({'message': 'error'})

@blueprint_company.route("/", methods=["POST"])
def create_company():
    repo = CompanyRepository(DBConnectionHandler)

    json_input = request.json
    param_company_id = json_input['company_id']

    try:
        data = repo.create_new_company(param_company_id)
        return jsonify({'message': 'ok'})
    except EntityAlreadyExists as e:
        return jsonify({'message': str(e)})
    except Exception:
        return jsonify({'message': 'error'})


@blueprint_company.route("/", methods=["DELETE"])
def delete_company():
    repo = CompanyRepository(DBConnectionHandler)
    query_param_company_id = request.args.get('company_id')

    try:
        data = repo.delete_company(query_param_company_id)
        return jsonify({'message': data})
    except Exception:
        return jsonify({'message': 'error'})
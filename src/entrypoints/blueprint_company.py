from flask import Blueprint, jsonify, request

from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.config.exceptions import EntityAlreadyExists
from src.infrastructure.repository.company_repository import CompanyRepository
from src.use_cases.create_company.create_company_use_case import CreateCompanyUseCase
from src.use_cases.delete_company.delete_company_use_case import DeleteCompanyUseCase
from src.use_cases.get_company.get_company_use_case import GetCompanyUseCase

from .blueprint_products import blueprint_products

# Defining blueprint
blueprint_company = Blueprint(name="blueprint_company", import_name=__name__)

# Nested blueprint register to access the URI: /company/products
blueprint_company.register_blueprint(blueprint_products)


@blueprint_company.route("/", methods=["GET"])
def get_company():
    try:
        uc = GetCompanyUseCase()
        repo = CompanyRepository(DBConnectionHandler)

        query_param_company_id = request.args.get("company_id")

        response = uc.get_company(repo, query_param_company_id)
        return response
    except Exception:
        return jsonify({"message": "Error"})


@blueprint_company.route("/", methods=["POST"])
def create_company():
    try:
        uc = CreateCompanyUseCase()
        repo = CompanyRepository(DBConnectionHandler)

        json_input = request.json
        param_company_id = json_input["company_id"]

        data = uc.create_company(repo, param_company_id)
        return jsonify({"message": data})
    except EntityAlreadyExists as e:
        return jsonify({"message": str(e)})
    except Exception:
        return jsonify({"message": "Error"})


@blueprint_company.route("/", methods=["DELETE"])
def delete_company():
    try:
        uc = DeleteCompanyUseCase()
        repo = CompanyRepository(DBConnectionHandler)

        query_param_company_id = request.args.get("company_id")

        data = uc.delete_company(repo, query_param_company_id)
        return jsonify({"message": data})
    except Exception:
        return jsonify({"message": "Error"})

"""
application factory
"""
from dotenv import dotenv_values
from flask import Flask

import src.infrastructure.entities.orm as ORM
from src.blueprint.blueprint_company import blueprint_company
from src.blueprint.blueprint_recharges import blueprint_recharges


def create_app():
    app = Flask(__name__)

    # Configuration via env variables
    config_env = dotenv_values(".env")['CONFIG_ENV']
    app.config.from_object(config_env)

    print(f"[+] Environment: {app.config['ENV']}")
    print(f"[+] Debug: {app.config['DEBUG']}")
    print(f"[+] Testing: {app.config['TESTING']}")

    # Register blueprint
    app.register_blueprint(blueprint_company, url_prefix="/company")
    app.register_blueprint(blueprint_recharges, url_prefix='/recharge')

    # configure mappers
    ORM.configure_mappers()

    return app

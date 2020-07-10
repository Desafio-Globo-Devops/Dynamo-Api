from project.core.schema import DynamoSchema #noqa
from flask_restx import Namespace

BASE_ROUTE = "logs"


def register_routes(api, app, root="api"):
    from.controller import api as dynamo_api

    api.add_namespace(dynamo_api, path=f"/{root}/{BASE_ROUTE}")
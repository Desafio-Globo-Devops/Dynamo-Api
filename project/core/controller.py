import base64

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from project.core.schema import DynamoSchema
from project.core.service import DynamoService

api = Namespace("Dynamo",
                description="Dynamo entity")  # noqa


@api.route("/")
class DynamoResource(Resource):
    """Dynamo"""

    @responds(schema=DynamoSchema)
    def get(self) -> DynamoSchema:
        """Get all logs Dynamo"""
        return DynamoService.get_logs()


@api.route("/<string:id>")
@api.param("id", "Enter Log ID")
class IdDynamo(Resource):

    @responds(schema=DynamoSchema)
    def get(self, id: str):
        """Get logs by ID Dynamo"""
        return DynamoService.get_logs_id(id)

    def delete(self, id: str):
        """Delete log by ID Dynamo"""
        return DynamoService.delete_logs_id(id)

    @accepts(schema=DynamoSchema, api=api)
    def put(self, id: str):
        """Put atributtes to logs Dynamo"""
        return DynamoService.put_log(id, request)

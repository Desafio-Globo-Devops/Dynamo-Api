import requests
import re
import json
import os
import boto3
from unicodedata import normalize
from flask import jsonify, request
from project.core.interface import DynamoInterface

access = {
    "region": os.getenv("AWS_DEFAULT_REGION"),
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY")
}
table = os.environ['TABLE']
dynamo_client = boto3.client('dynamodb',
                             aws_access_key_id=f"{access['aws_access_key_id']}",
                             aws_secret_access_key=f"{access['aws_secret_access_key']}",
                             region_name=f"{access['region']}")


class DynamoService():

    @staticmethod
    def get_logs():
        return jsonify(dynamo_client.scan(
            TableName=table
        )["Items"])

    @staticmethod
    def get_logs_id(id: str):
        resp = dynamo_client.get_item(
            TableName=table,
            Key={
                'ID': {'S': id}
            }
        )
        item = resp.get('Item')
        if not item:
            return jsonify({'error': 'Log does not exist'}), 404

        print(item)
        return jsonify(item)

    @staticmethod
    def put_log(request):
        newInfo = request.json['newInfo']
        Obs = request.json['Obs']
        resp = dynamo_client.get_item(
            TableName=table,
            Key={
                'ID': {'S': id}
            }
        )
        item = resp.get('Item')
        if not item:
            return jsonify({'error': 'Log does not exist'}), 404
        response = dynamo_client.update_item(
            TableName=table,
            Key={
                'ID': {'S': id}
            },
            UpdateExpression='SET newInfo = :newInfo, Obs = :Obs',
            ExpressionAttributeValues={
                ':newInfo': {'S': newInfo},
                ':Obs': {'S': Obs}
            },
            ReturnValues="UPDATED_NEW"
        )
        return jsonify(response, {'UPDATE!': 'Log was updated!'})

    @staticmethod
    def delete_logs_id(id):
        resp = dynamo_client.get_item(
            TableName=table,
            Key={
                'ID': {'S': id}
            }
        )
        item = resp.get('Item')
        if not item:
            return jsonify({'error': 'Log does not exist'}), 404
        response = dynamo_client.delete_item(
            TableName=table,
            Key={
                'ID': {'S': id}
            }
        )
        return jsonify({'DELETED!': 'Log was deleted!'})

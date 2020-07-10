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
    def put_log(id, request):
        awsRegion = request.json['awsRegion']
        eventID = request.json['eventID']
        eventName = request.json['eventName']
        eventSource = request.json['eventSource']
        eventType = request.json['eventType']
        eventVersion = request.json['eventVersion']
        recipientAccountId = request.json['recipientAccountId']
        requestID = request.json['requestID']
        sourceIPAddress = request.json['sourceIPAddress']
        userAgent = request.json['userAgent']
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
            UpdateExpression='SET awsRegion = :awsRegion, eventID = :eventID, '
                             'eventName = :eventName, eventSource = '
                             ':eventSource, eventType = :eventType, '
                             'eventVersion = :eventVersion, '
                             'recipientAccountId = :recipientAccountId, '
                             'requestID = :requestID, sourceIPAddress = '
                             ':sourceIPAddress, userAgent = :userAgent',
            ExpressionAttributeValues={
                ':awsRegion': {'S': awsRegion},
                ':eventID': {'S': eventID},
                ':eventName': {'S': eventName},
                ':eventSource': {'S': eventSource},
                ':eventType': {'S': eventType},
                ':eventVersion': {'S': eventVersion},
                ':recipientAccountId': {'S': recipientAccountId},
                ':requestID': {'S': requestID},
                ':sourceIPAddress': {'S': sourceIPAddress},
                ':userAgent': {'S': userAgent}

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

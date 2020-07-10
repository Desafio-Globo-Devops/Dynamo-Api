from marshmallow import fields, Schema


class DynamoSchema(Schema):
    ''' Dynamo schema'''

    awsRegion = fields.String(attribute='awsRegion')
    eventID = fields.String(attribute='eventID')
    eventName = fields.String(attribute='eventName')
    eventSource = fields.String(attribute='eventSource')
    eventType = fields.String(attribute='eventType')
    eventVersion = fields.String(attribute='eventVersion')
    recipientAccountId = fields.String(attribute='recipientAccountId')
    requestID = fields.String(attribute='requestID')
    sourceIPAddress = fields.String(attribute='sourceIPAddress')
    userAgent = fields.String(attribute='userAgent')

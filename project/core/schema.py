from marshmallow import fields, Schema


class DynamoSchema(Schema):
    ''' Dynamo schema'''

    id = fields.String(attribute='id')

from marshmallow import Schema, fields, validate


class Person(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=1))
    birthday = fields.Date(required=True)


class FilterPersons(Schema):
    id = fields.Int()
    name = fields.Str(validate=validate.Length(min=1))
    birthday = fields.Date()

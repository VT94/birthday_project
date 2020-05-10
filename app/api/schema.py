from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(1))
    birthday = fields.Date(required=True)


class SchemaShow(Schema):
    name = fields.Str()
    birthday = fields.Date()
    id = fields.Int()


schema_add = PersonSchema()
schema_del = PersonSchema()
schema_del.birthday = fields.Date(required=False)
schema_show = SchemaShow()
schema_test = Schema()
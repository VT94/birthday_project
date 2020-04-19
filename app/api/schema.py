from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(1))
    birthday = fields.Date(required=True)

    async def validate_in(self, payload):
        record = self.load(payload)
        return record


schema_add = PersonSchema()
schema_del = PersonSchema()
schema_del.birthday = fields.Date(required=False)
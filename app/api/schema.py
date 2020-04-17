from marshmallow import Schema, fields, validate


class PersonSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(1))
    birthday = fields.Date(required=True)

    async def validate_in(self, payload):
        try:
            record = self.load(payload)
        except Exception as err:
            print(err)


schema_add = PersonSchema()

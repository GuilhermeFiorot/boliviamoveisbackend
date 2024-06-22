from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)
    is_admin = fields.Bool(dump_only=True)
    endereco = fields.Str(required=True)
    cidade = fields.Str(required=True)
    cep = fields.Str(required=True)
    pais = fields.Str(required=True)
    telefone = fields.Str(required=True)
    cpf = fields.Str(required=True)
from marshmallow import Schema, fields, post_load, validates, ValidationError
from app.models import Usuario

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=lambda x: len(x) > 0)
    email = fields.Email(required=True)
    edad = fields.Int(allow_none=True, validate=lambda x: x > 0 if x else True)
    password  = fields.Str(requiered=True , validate=lambda x: len(x)> 0)
    
    @post_load
    def make_usuario(self, data, **kwargs):
        return Usuario(**data)
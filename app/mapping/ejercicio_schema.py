from marshmallow import Schema, fields, post_load, validates, ValidationError
from app.models import Ejercicio
from app.models import GrupoMuscular

# Schema para Ejercicio
class EjercicioSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=lambda x: len(x) > 0)
    descripcion = fields.Str(allow_none=True)
    grupo_muscular_id = fields.Int(required=True)
    
    @post_load
    def make_ejercicio(self, data, **kwargs):
        return Ejercicio(**data)
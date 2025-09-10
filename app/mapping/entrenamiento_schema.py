from marshmallow import Schema, fields, post_load, validates, ValidationError
from app.models import Entrenamiento

class EntrenamientoSchema(Schema):
    id = fields.Int(dump_only=True)
    grupo_muscular_id = fields.Int(required=True)
    ejercicio_id = fields.Int(required=True)
    fecha = fields.Date(dump_only=True)
    repeticiones = fields.Int(required=True)
    peso = fields.Float(allow_none=True)
    
    
    @post_load
    def make_entrenamiento(self, data, **kwargs):
        return Entrenamiento(**data)
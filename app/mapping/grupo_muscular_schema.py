from marshmallow import Schema, fields, post_load, validates, ValidationError
from app.models.grupo_muscular import GrupoMuscular

# Schema para Grupo Muscular
class GrupoMuscularSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=lambda x: len(x) > 0)
    descripcion = fields.Str(allow_none=True)
    
    @post_load
    def make_grupo_muscular(self, data, **kwargs):
        return GrupoMuscular(**data)
from app.models.grupo_muscular import GrupoMuscular
from app.extensions import  db

class GrupoMuscularRepository:

    @staticmethod
    def create(nombre):
        grupo = GrupoMuscular(nombre=nombre)
        db.session.add(grupo)
        db.session.commit()
        return grupo

    @staticmethod
    def get_all():
        return GrupoMuscular.query.all()

    @staticmethod
    def get_by_id(grupo_id):
        return GrupoMuscular.query.get(grupo_id)

    @staticmethod
    def update(grupo_id, nombre=None):
        grupo = GrupoMuscular.query.get(grupo_id)
        if not grupo:
            return None
        if nombre:
            grupo.nombre = nombre
        db.session.commit()
        return grupo

    @staticmethod
    def delete(grupo_id):
        grupo = GrupoMuscular.query.get(grupo_id)
        if not grupo:
            return None
        db.session.delete(grupo)
        db.session.commit()
        return True

from app.models.entrenamiento import Entrenamiento
from app.extensions import  db
#from database import db

class EntrenamientoRepository:

    @staticmethod
    def create(usuario_id, ejercicio_id, repeticiones, fecha):
        entrenamiento = Entrenamiento(
            usuario_id=usuario_id,
            ejercicio_id=ejercicio_id,
            repeticiones=repeticiones,
            fecha=fecha
        )
        db.session.add(entrenamiento)
        db.session.commit()
        return entrenamiento

    @staticmethod
    def get_all():
        return Entrenamiento.query.all()

    @staticmethod
    def get_by_id(entrenamiento_id):
        return Entrenamiento.query.get(entrenamiento_id)

    @staticmethod
    def update(entrenamiento_id, repeticiones=None, fecha=None):
        entrenamiento = Entrenamiento.query.get(entrenamiento_id)
        if not entrenamiento:
            return None
        if repeticiones:
            entrenamiento.repeticiones = repeticiones
        if fecha:
            entrenamiento.fecha = fecha
        db.session.commit()
        return entrenamiento

    @staticmethod
    def delete(entrenamiento_id):
        entrenamiento = Entrenamiento.query.get(entrenamiento_id)
        if not entrenamiento:
            return None
        db.session.delete(entrenamiento)
        db.session.commit()
        return True

from app.models.ejercicio import Ejercicio
from app.extensions import  db
#from database import db

class EjercicioRepository:

    @staticmethod
    def create(nombre, grupo_muscular_id):
        ejercicio = Ejercicio(nombre=nombre, grupo_muscular_id=grupo_muscular_id)
        db.session.add(ejercicio)
        db.session.commit()
        return ejercicio

    @staticmethod
    def get_all():
        return Ejercicio.query.all()

    @staticmethod
    def get_by_id(ejercicio_id):
        return Ejercicio.query.get(ejercicio_id)

    @staticmethod
    def update(ejercicio_id, nombre=None, grupo_muscular_id=None):
        ejercicio = Ejercicio.query.get(ejercicio_id)
        if not ejercicio:
            return None
        if nombre:
            ejercicio.nombre = nombre
        if grupo_muscular_id:
            ejercicio.grupo_muscular_id = grupo_muscular_id
        db.session.commit()
        return ejercicio

    @staticmethod
    def delete(ejercicio_id):
        ejercicio = Ejercicio.query.get(ejercicio_id)
        if not ejercicio:
            return None
        db.session.delete(ejercicio)
        db.session.commit()
        return True

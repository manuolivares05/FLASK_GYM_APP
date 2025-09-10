from app.models.usuario import Usuario
from app.extensions import  db
from typing import List, Optional


class UsuarioRepository:

    @staticmethod
    def create(usuario:Usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def get_all(self, page: int = 1, per_page: int = 20):
        """Devuelve los usuarios con paginación."""
        return Usuario.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_id(usuario_id):
        """Busca un usuario por su ID"""
        return Usuario.query.get(usuario_id)

    @staticmethod
    def update(usuario_id, nombre=None, email=None):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return None
        if nombre:
            usuario.nombre = nombre
        if email:
            usuario.email = email
        db.session.commit()
        return usuario

    @staticmethod
    def delete(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return None
        db.session.delete(usuario)
        db.session.commit()
        return True
    
    def get_by_username(self, usuario: str) -> Optional[Usuario]:
        """Devuelve un usuario por su nombre"""
        return Usuario.query.filter_by(nombre=usuario).first()
    
    def get_by_email(self, email: str) -> Optional[Usuario]:
        """Busca un usuario por su email"""
        return Usuario.query.filter_by(email=email).first()
    


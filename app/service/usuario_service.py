from typing import Optional, List
from app.models.usuario import Usuario
from app.mapping.usuario_schema import UsuarioSchema
from app.repository.usuario_repository import UsuarioRepository
from app.extensions import  db

class UsuarioService:
    def __init__(self, repo: UsuarioRepository = None):
        self.repo = repo or UsuarioRepository()
        self.schema =  UsuarioSchema()

    def crear_usuario(self, data:dict)-> Usuario:
        """
        Recibe un diccionario con los datos, 
        lo valida y convierte en un objetSo Category.
        """
        # 1. Validar + deserializar (dict → Category)
        usuario: Usuario = self.schema.load(data)
        return self.repo.create(usuario)
    
    def obtener_usuario_id(self, user_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por su ID"""
        return self.repo.get_by_id(user_id)
    
    def obtener_usuario(self, usuario: str) -> Optional[Usuario]:
        """Obtiene un usuario por su nombre de usuario"""
        return self.repo.get_by_username(usuario)
    
    def autentificacion(self,usuario:str, password:str)-> Optional[Usuario]:
        """Verifica credenciales: intenta por username, si no busca email. Devuelve el User si coincide, o None"""

        ser = self.repo.get_by_username(usuario) or self.repo.get_by_email(usuario)
        if usuario and usuario.check_password(password):
            return usuario
        return None

    def lista_usuario(self, page: int = 1, per_page: int = 20) -> List[Usuario]:
        """Lista usuarios paginados"""
        return self.repo.get_all(page=page, per_page=per_page)
    
    def update_usuario(self, user_id: int, **updates) -> Optional[Usuario]:
        user = self.repo.get_by_id(user_id)
        if not user:
            return None

        allowed = {"nombre", "email", "contraseña"}
        data = {k: v for k, v in updates.items() if k in allowed}
        if not data:
            return user

        if "contraseña" in data:
            user.contraseña = data.pop("contraseña")

        return self.repo.update(user, **data)

    def borra_usuario(self, user_id: int) -> bool:
        user = self.repo.get_by_id(user_id)
        if not user:
            return False
        self.repo.delete(user)
        return True




    

     


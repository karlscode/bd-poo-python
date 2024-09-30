from database.connection import get_session
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.session = get_session()
        self.repository = UsuarioRepository(self.session)

    def create_usuario(self, nome, email, senha):
        return self.repository.create(nome, email, senha)

    def get_all_usuarios(self):
        return self.repository.get_all()

    def update_usuario(self, usuario_id, **kwargs):
        return self.repository.update(usuario_id, **kwargs)

    def delete_usuario(self, usuario_id):
        return self.repository.delete(usuario_id)

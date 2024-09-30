from database.connection import engine
from models.usuario import Base as UsuarioBase
from models.livro import Base as LivroBase
from services.usuario_service import UsuarioService
from services.livro_service import LivroService

# Criação das tabelas
UsuarioBase.metadata.create_all(bind=engine)
LivroBase.metadata.create_all(bind=engine)

if __name__ == "__main__":
    usuario_service = UsuarioService()
    livro_service = LivroService()

    usuario = usuario_service.create_usuario("Lira", "qlqcoisa@email.com", "123123")
    print(f"Usuário criado: {usuario.nome}")

    livro = livro_service.create_livro("Nome do Vento", 1000, usuario.id)
    print(f"Livro criado: {livro.titulo}")

    # Update usuário
    updated_usuario = usuario_service.update_usuario(usuario.id, nome="João Lira")
    print(f"Usuário atualizado: {updated_usuario.nome}")

    # Delete livro
    livro_service.delete_livro(livro.id)
    print(f"Livro deletado com ID: {livro.id}")

    # Delete usuário
    usuario_service.delete_usuario(usuario.id)
    print(f"Usuário deletado com ID: {usuario.id}")

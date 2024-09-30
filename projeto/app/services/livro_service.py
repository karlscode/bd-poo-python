from database.connection import get_session
from repositories.livro_repository import LivroRepository

class LivroService:
    def __init__(self):
        self.session = get_session()
        self.repository = LivroRepository(self.session)

    def create_livro(self, titulo, qtde_paginas, dono):
        return self.repository.create(titulo, qtde_paginas, dono)

    def update_livro(self, livro_id, **kwargs):
        return self.repository.update(livro_id, **kwargs)

    def delete_livro(self, livro_id):
        return self.repository.delete(livro_id)

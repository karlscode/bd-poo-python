from sqlalchemy.orm import Session
from models.livro import Livro

class LivroRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, titulo, qtde_paginas, dono):
        livro = Livro(titulo=titulo, qtde_paginas=qtde_paginas, dono=dono)
        self.session.add(livro)
        self.session.commit()
        return livro

    def update(self, livro_id, **kwargs):
        livro = self.session.query(Livro).filter(Livro.id == livro_id).first()
        for key, value in kwargs.items():
            setattr(livro, key, value)
        self.session.commit()
        return livro

    def delete(self, livro_id):
        livro = self.session.query(Livro).filter(Livro.id == livro_id).first()
        if livro:
            self.session.delete(livro)
            self.session.commit()

from sqlalchemy.orm import Session
from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, nome, email, senha):
        usuario = Usuario(nome=nome, email=email, senha=senha)
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def get_all(self):
        return self.session.query(Usuario).all()

    def update(self, usuario_id, **kwargs):
        usuario = self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
        for key, value in kwargs.items():
            setattr(usuario, key, value)
        self.session.commit()
        return usuario

    def delete(self, usuario_id):
        usuario = self.session.query(Usuario).filter(Usuario.id == usuario_id).first()
        if usuario:
            self.session.delete(usuario)
            self.session.commit()

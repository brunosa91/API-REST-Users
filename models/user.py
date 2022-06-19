from db import db

class UserModel(db.model):
    __tablename__ = 'users'

    id = db.Collumn(db.intenger, primary_key = True)
    nome = db.Collumn(db.String(80), nullable=False, unique = True)
    email = db.Collumn(db.String(80), nullable=False, unique = True)
    telefone = db.Collumn(db.intenger, nullable=False)

    def __init__(self,nome,email,telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repre__(self, ):
        return f'UserModel(nome={self.nome},email={self.email},telefone={self.telefone})'

   

from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80), nullable=False, unique = True)
    email = db.Column(db.String(80), nullable=False, unique = True)
    telefone = db.Column(db.Integer, nullable=False)

    def __init__(self,nome,email,telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repre__(self, ):
        return f'UserModel(nome={self.nome},email={self.email},telefone={self.telefone})'

    def json(self,):
       return{
           'nome':self.nome,
           'email':self.email,
           'telefone':self.telefone
       }

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, ):
        db.session.delete(self)
        db.session.commit()
        
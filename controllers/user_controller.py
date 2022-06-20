from flask import request
from flask_restx import Resource, fields
from models.user import UserModel
from schemas.users import UserSchema

from server.instance import server

user_ns = server.user_ns
user_schema = UserSchema() 
list_user_schema = UserSchema(many =True)

ITEM_NOT_FOUND = 'Usuário não encontrado'

item = user_ns.model('UserModel',{
    'nome':fields.String(description='Nome do usuário'),
    'email':fields.String(description='Email do usuário'),
    'telefone':fields.Integer(default=0)
})

class User(Resource):
    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data),200
        return{'message': ITEM_NOT_FOUND}, 404

    

class UserEdit(Resource):
    @user_ns.expect(item)
    def put(self, id):
        user_data = UserModel.find_by_id(id)
        user_json = request.get_json()

        user_data.nome = user_json['nome']
        user_data.email = user_json['email']
        user_data.telefone = user_json['telefone']

        user_data.save_to_db()
        return user_schema.dump(user_data), 200
    
    


class UserDelete(Resource):
    @user_ns.expect(item)
    def delete(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            user_data.delete_from_db()
            return '', 204
        return {'message', ITEM_NOT_FOUND}


class UserList(Resource):
    def get(self, ):
        return list_user_schema.dump(UserModel.find_all()),200
    
 

class UserAdd(Resource):
    @user_ns.expect(item)
    @user_ns.doc('Create an item')
    
    def post(self, ):
        user_json = request.get_json()
        user_data=user_schema.load(user_json)

        user_data.save_to_db()

        return user_schema.dump(user_data), 201
        

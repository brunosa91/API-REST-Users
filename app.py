from flask import Flask, Blueprint, jsonify
from flask_restx import Api
from ma import ma
from db import db
from marshmallow import ValidationError
from controllers.user_controller import User, UserList, UserAdd,UserDelete,UserEdit

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User,'/users/<int:id>')
api.add_resource(UserList,'/users')
api.add_resource(UserAdd,'/add_users')
api.add_resource(UserDelete,'/delete_user/<int:id>')
api.add_resource(UserEdit,'/edit_user/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()


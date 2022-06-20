from ma import ma
from models.user import UserModel
# from ma import SQLAlchemyAutoSchema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
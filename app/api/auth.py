from flask_restful import Resource
from flask import request
from ..services.user_service import get_user_by_email, check_password, create_user
from ..schemas.user import UserSchema
from flask_jwt_extended import create_access_token

user_schema = UserSchema()

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = get_user_by_email(data['email'])
        if user and check_password(user, data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        user = get_user_by_email(data['email'])
        if user:
            return {"message": "User already exists"}, 400
        new_user = create_user(data)
        access_token = create_access_token(identity=new_user.id)
        return {"access_token": access_token}, 201
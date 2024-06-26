from flask_restful import Resource
from flask import request
from ..services.user_service import get_user_by_email, update_user
from ..schemas.user import UserSchema

user_schema = UserSchema()

class ForgotPasswordResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        new_password = data.get('password')
        
        user = get_user_by_email(email)
        if user is None:
            return {"message": "User not found"}, 404
        
        user_data = {"password": new_password}
        update_user(user, user_data)
        return {"message": "Password updated successfully"}, 200
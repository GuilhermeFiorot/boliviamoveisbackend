from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from ..services.user_service import get_all_users, get_user_by_id, create_user, update_user, delete_user
from ..schemas.user import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        users = get_all_users()
        return users_schema.dump(users), 200

    #def post(self):
    #    data = request.get_json()
    #    user = create_user(data)
    #    return user_schema.dump(user), 201

class UserResource(Resource):
    @jwt_required()
    def get(self, id):
        user = get_user_by_id(id)
        if user is None:
            return {"message": "User not found"}, 404
        return user_schema.dump(user), 200

    @jwt_required()
    def put(self, id):
        user = get_user_by_id(id)
        if user is None:
            return {"message": "User not found"}, 404
        data = request.get_json()
        user = update_user(user, data)
        return user_schema.dump(user), 200

    @jwt_required()
    def delete(self, id):
        user = get_user_by_id(id)
        if user is None:
            return {"message": "User not found"}, 404
        delete_user(user)
        return {"message": "User deleted"}, 204
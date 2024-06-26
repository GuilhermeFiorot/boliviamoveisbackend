from flask import Blueprint
from flask_restful import Api
from .product import ProductListResource, ProductResource
from .user import UserListResource, UserResource
from .auth import LoginResource, RegisterResource
from .cart import CartResource
from .forgot_password import ForgotPasswordResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(ProductListResource, '/v1/products')
api.add_resource(ProductResource, '/v1/products/<int:id>')

api.add_resource(UserListResource, '/v1/users')
api.add_resource(UserResource, '/v1/users/<int:id>')

api.add_resource(LoginResource, '/v1/login')
api.add_resource(RegisterResource, '/v1/register')
api.add_resource(ForgotPasswordResource, '/v1/forgot_password')

api.add_resource(CartResource, '/v1/cart')
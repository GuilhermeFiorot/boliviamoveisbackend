from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.cart_service import get_cart_by_user, add_item_to_cart, remove_item_from_cart
from ..schemas.cart import CartSchema, CartItemSchema

cart_schema = CartSchema()
cart_item_schema = CartItemSchema()

class CartResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        cart = get_cart_by_user(user_id)
        return cart_schema.dump(cart), 200

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        cart_item = add_item_to_cart(user_id, data["product_id"], data["quantity"])
        return cart_item_schema.dump(cart_item), 201

    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()
        data = request.get_json()
        success = remove_item_from_cart(user_id, data["product_id"])
        if success:
            return {"message": "Item removed from cart"}, 204
        return {"message": "Item not found in cart"}, 404
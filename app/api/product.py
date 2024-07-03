from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required  # Add this line
from ..services.product_service import get_all_products, get_product_by_id, create_product, update_product, delete_product
from ..schemas.product import ProductSchema
from ..constants import PRODUCT_NOT_FOUND

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class ProductListResource(Resource):
    def get(self):
        products = get_all_products()
        return products_schema.dump(products), 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        product = create_product(data)
        return product_schema.dump(product), 201

class ProductResource(Resource):
    @jwt_required()
    def get(self, id):
        product = get_product_by_id(id)
        if product is None:
            return {"message": PRODUCT_NOT_FOUND}, 404
        return product_schema.dump(product), 200

    @jwt_required()
    def put(self, id):
        product = get_product_by_id(id)
        if product is None:
            return {"message": PRODUCT_NOT_FOUND}, 404
        data = request.get_json()
        product = update_product(product, data)
        return product_schema.dump(product), 200

    @jwt_required()
    def delete(self, id):
        product = get_product_by_id(id)
        if product is None:
            return {"message": PRODUCT_NOT_FOUND}, 404
        delete_product(product)
        return {"message": "Product deleted"}, 204
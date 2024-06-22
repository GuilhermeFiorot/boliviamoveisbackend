from ..models.product import Product
from ..core.database import db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return db.session.get(Product, product_id)

def create_product(data):
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product, data):
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product

def delete_product(product):
    db.session.delete(product)
    db.session.commit()
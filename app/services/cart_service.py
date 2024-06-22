from ..models.cart_item import CartItem
from ..models.product import Product
from ..core.database import db

def get_cart_by_user(user_id):
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    cart = {"items": [], "total_value": 0.0}
    for item in cart_items:
        single_value = item.product.price
        total_value = single_value * item.quantity
        cart["items"].append({
            "product_id": item.product.id,
            "quantity": item.quantity,
            "single_value": single_value,
            "total_value": total_value
        })
        cart["total_value"] += total_value
    return cart

def add_item_to_cart(user_id, product_id, quantity):
    cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    db.session.commit()
    return cart_item

def remove_item_from_cart(user_id, product_id):
    cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return True
    return False
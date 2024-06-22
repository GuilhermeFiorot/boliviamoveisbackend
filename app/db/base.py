from ..core.database import db

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Import all models here so Alembic can recognize them during migrations
from ..models.user import User
from ..models.product import Product
from ..models.cart_item import CartItem
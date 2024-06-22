from marshmallow import Schema, fields

class CartItemSchema(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    single_value = fields.Float(dump_only=True)
    total_value = fields.Float(dump_only=True)

class CartSchema(Schema):
    items = fields.List(fields.Nested(CartItemSchema))
    total_value = fields.Float(dump_only=True)
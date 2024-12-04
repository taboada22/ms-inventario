from marshmallow import validate, fields, Schema, post_load
from app.models import Stock
from datetime import datetime

class StockSchema(Schema):
    id_stock = fields.Integer(dump_only=True)
    id_product = fields.Integer(required=True)
    date_transaction = fields.DateTime(load_default=datetime.today())
    amount = fields.Float(required=True, validate=validate.Range(min=0))
    input_output = fields.Integer(required=False, validate=validate.OneOf([1, 2]))

    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)
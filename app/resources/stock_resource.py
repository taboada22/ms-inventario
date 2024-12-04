from flask import Blueprint, request, jsonify
from app.services.stock_services import StockService
from app.schemas.stock_schema import StockSchema

stock = Blueprint('stock', __name__, url_prefix='/api/stock')
service = StockService()

stock_schema = StockSchema()

@stock.route('/enter_product', methods=['POST'])
def enter_product():
    stock_data = stock_schema.load(request.json)
    stock_data = service.enter(stock_data)
    return stock_schema.dump(stock_data), 200

@stock.route('/whitdraw', methods=['POST'])
def whitdraw_product():
    stock_data = stock_schema.load(request.json)
    stock_data = service.withdraw(stock_data)
    return stock_schema.dump(stock_data), 200

@stock.route('/find_by_id/<int:id>', methods=['GET'])
def get_stock(id):
    stock = stock_schema.dump(service.get_stock(id))
    if stock is None:
        return jsonify({'message': 'Not found'}), 404
    return stock

@stock.route('/calculate_stock/<int:product_id>', methods=['GET'])
def calculate_stock(product_id):
    stock = service.calculate_stock(product_id)
    return jsonify({'total_stock': stock}), 200

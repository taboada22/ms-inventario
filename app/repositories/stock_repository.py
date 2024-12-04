from app import db
from app.models.stock import Stock
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy import func

class StockRepository:
    def save(self, stock: Stock) -> Stock:
        try:
            db.session.add(stock) 
            db.session.commit()
            return stock
        except IntegrityError:
            db.session.rollback()
            print("Rollback en repository 1")
            

            
    def find_by_id(self, id: int) -> Stock :
        try:
            return db.session.query(Stock).filter(Stock.id_stock == id).one()
        except NoResultFound:
            return None

    def find_product_by_id(self, id: int) -> Stock :
        try:
            return db.session.query(Stock).filter(Stock.id_product == id).all()
        except NoResultFound:
            return None
        
    def get_stock_by_product(self, product:int):
        result = db.session.query(Stock).filter()
    

from dataclasses import dataclass
from app import db
from datetime import datetime


@dataclass
class Stock(db.Model):
    
    __tablename__ = 'stocks'

    id_stock= db.Column('id_stock', db.Integer, primary_key=True, autoincrement=True)
    id_product = db.Column('id_product', db.Integer, nullable=False)
    date_transaction= db.Column('date_transaction', db.DateTime, nullable=False, default=datetime.now())
    amount = db.Column('amount', db.Integer, nullable=False)
    input_output = db.Column('input_output', db.Integer, nullable=False) # 1: entrada - 2: salida
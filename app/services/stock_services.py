from app.models.stock import Stock
from app.repositories.stock_repository import StockRepository
from app import cache
from app import cache
from threading import Lock, current_thread
from multiprocessing import Lock as work_lock

locker = Lock() 
worker_lock = work_lock() 


class StockService:
    def __init__(self):
        self.repository = StockRepository()

    def withdraw(self, stock_data: Stock) -> Stock:
        worker_lock.acquire()
        locker.acquire()
        result = None
        if stock_data is not None:
            existing_stock = self.repository.find_by_id(stock_data.id_stock)
            
            if existing_stock:
                existing_stock.amount -= stock_data.amount
                existing_stock.input_output = 2  
                result = self.repository.save(existing_stock)
            else:
                stock_data.input_output = 2  
                result = self.repository.save(stock_data)

            cache.set(f'stock_{stock_data.id_stock}', result, timeout=60)
        locker.release()
        worker_lock.release()
        return result

    def enter(self, stock_data: Stock) -> Stock:
        existing_stock = self.repository.get_stock_by_product(stock_data.id_product)
            
        if existing_stock:
            existing_stock.amount += stock_data.amount
            existing_stock.input_output = 1  
            result = self.repository.save(existing_stock)
        else:
            stock_data.input_output = 1  
            result = self.repository.save(stock_data)

        cache.set(f'stock_{stock_data.id_stock}', result, timeout=60)
        return result
    
    def calculate_stock(self, product_id: int) -> int:
        
        product_stocks = self.repository.find_product_by_id(product_id)
        
        input_quantity = 0
        output_quantity = 0
        
        for stock in product_stocks:
            if stock.input_output == 1:
                input_quantity += stock.amount
            elif stock.input_output == 2:
                output_quantity += stock.amount
        
        stock = input_quantity - output_quantity
        
        return stock
    
    def get_stock(self, stock_id: int) -> Stock:
        return self.repository.find_by_id(stock_id)

   
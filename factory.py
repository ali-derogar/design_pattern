from abc import ABCMeta , abstractmethod

# simple factory 

class Book(metaclass = ABCMeta):
    
    def __init__(self , price , count) -> None:
        self.count = count
        self.price = price
        self.cost = \
            count * (price - ((count / price) * price)) \
            if count < 20 \
            else count * (price - ((25 / price) * price))
            
        return super().__init__()

    
    @abstractmethod
    def pages_of_book():
        pass
    
    @abstractmethod
    def get_book_price():
        pass
    
class HarryPotter(Book):
    
    def pages_of_book(self):
        print(423)
        
    def get_book_price(self):
        print(self.cost)

class WildCastle(Book):
    
    def pages_of_book(self):
        print(202) 
    
    def get_book_price(self):
        print(self.cost)
        
class BookPublicator():
    
    def get_book_pages_numbder(self,book_name):
        
        eval(book_name)(1 , 1).pages_of_book()
    
    def get_book_prices(self,book_name,price , count):
        
        eval(book_name)(price , count).get_book_price()
        
        

if __name__ == "__main__":
    
    b = BookPublicator()
    b.get_book_pages_numbder("HarryPotter")
    b.get_book_prices("HarryPotter",100,12)
    
# 423
# 1056.0
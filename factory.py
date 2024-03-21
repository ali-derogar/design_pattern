from abc import ABCMeta , abstractmethod , ABC

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

# client only work with this section
# 423
# 1056.0

# factory method


class Profile(ABC):
    
    def __init__(self):
        self.sections = []
        self.create_profile()
        
    @abstractmethod
    def create_profile():
        pass
    
    def add_profile(self,obj):
        self.sections.append(obj)
    
    def get_profile(self,obj):
        print(self.sections[obj])

class Section(ABC):
    
    @abstractmethod
    def describe():
        pass
    
class PersonalSection(Section):
    
    def describe():
        print("PersonalSection")
    
class CardSection(Section):
    
    def describe():
        print("CardSection")
        
class SearchSection(Section):
    
    def describe():
        print("CardSection")
        
class Linkedin(Profile):
    
    def create_profile(self):
        self.add_profile(PersonalSection())
        self.add_profile(SearchSection())
        
class ParsPack(Profile):
    
    def create_profile(self):
        self.add_profile(PersonalSection())
        self.add_profile(CardSection())
        self.add_profile(SearchSection())

p = ParsPack()
print(p.sections)


# abstarct factory

class CoffieFactory(ABC):
    
    @abstractmethod
    def create_coffie_without_milk():
        pass

    @abstractmethod
    def create_coffie_with_milk():
        pass
    
class CoffieWithMilk(ABC):
    
    @abstractmethod
    def serve():
        pass

class CoffieWithOutMilk(ABC):
    
    @abstractmethod
    def prepar():
        pass
     
class ItalianCoffieFactory(CoffieFactory):
    
    def create_coffie_with_milk(self):
        return ItalianCopuchino()
        
    def create_coffie_without_milk(self):
        return ItalianSperso()
    
class FrenchCoffieFactory(CoffieFactory):
    
    def create_coffie_with_milk(self):
        return FrenchCopuchino()
        
    def create_coffie_without_milk(self):
        return FrenchSperso()

class ItalianSperso(CoffieWithOutMilk):
    
    def prepar(self):
        print(type(self).__name__ , " sperso is praper ")
    
class ItalianCopuchino(CoffieWithMilk):
    
    def serve(self, name):
        print(type(self).__name__ , " with milk ",type(name).__name__)
    
class FrenchSperso(CoffieWithOutMilk):
    
    def prepar(self):
        print(type(self).__name__ , " sperso is praper ")
    
class FrenchCopuchino(CoffieWithMilk):
    
    def serve(self, name):
        print(type(self).__name__ , " with milk ",type(name).__name__)
    
class CoffieShop():
    
    def make_coffie(self):
        for factory in [ItalianCoffieFactory() ,FrenchCoffieFactory()]:
            
            coffie_without = factory.create_coffie_without_milk()
            coffie_with = factory.create_coffie_with_milk()
            coffie_without.prepar()
            coffie_with.serve(coffie_without)
        
        
c = CoffieShop()
c.make_coffie()

# ItalianSperso  sperso is praper 
# ItalianCopuchino  with milk  ItalianSperso
# FrenchSperso  sperso is praper 
# FrenchCopuchino  with milk  FrenchSperso
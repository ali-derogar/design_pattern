


class Subject:
    
    def __init__(self) -> None:
        self.__observers = []
        
    def register(self,observer):
        self.__observers.append(observer)
        
    def send_notif_all(self):
        
        for observer in self.__observers:
            observer.notify()
            
class Observer():
    
    def __init__(self ,subject ,messages) -> None:
        self.messages = messages
        subject.register(self)
        
    def notify(self):
        print(type(self).__name__ , " => " , self.messages)
        
sub = Subject()
ob1 = Observer(sub ,"type 1")
ob2 = Observer(sub ,"type 2")
sub.send_notif_all()

# Observer  =>  type 1
# Observer  =>  type 2

class Publisher:
    
    def __init__(self) -> None:
        self._latestbooks = None
        self._subscribers = []
        
    def register(self,sub):
        self._subscribers.append(sub)
        
    def deregister(self):
        self._subscribers.pop()
        
    def subscribers(self):
        for sub in self._subscribers:
            print(type(sub).__name__)
            
    def add_books(self,books):
        self._latestbooks = books
        
    def get_books(self):
        return self._latestbooks
    
    def send_notif_all(self):
        for sub in self._subscribers:
            print(sub.notify())
            
from abc import ABCMeta , abstractmethod
class Subscribers(metaclass =ABCMeta):
    @abstractmethod
    def notify(self):
        pass
    
class SmsSub(Subscribers):
    
    def __init__(self,publisher) -> None:
        self.publisher = publisher
        self.publisher.register(self)
        
    def notify(self):
        return f"{type(self).__name__} , new books = {self.publisher.get_books()}"
    
class EmailSub(Subscribers):
    
    def __init__(self,publisher) -> None:
        self.publisher = publisher
        self.publisher.register(self)
        
    def notify(self):
        return f"{type(self).__name__} , new books = {self.publisher.get_books()}"
    
class OthersSub(Subscribers):
    
    def __init__(self,publisher) -> None:
        self.publisher = publisher
        self.publisher.register(self)
        
    def notify(self):
        return f"{type(self).__name__} , new books = {self.publisher.get_books()}"
    
print("*"*100)
pub = Publisher()
for sub in [SmsSub ,  EmailSub ,  OthersSub]:
    sub(pub)
    
pub.subscribers()
pub.add_books(["harry potter" , "lord of the ring"])
pub.send_notif_all()
pub.deregister()
pub.subscribers()
pub.add_books(["magic"])
pub.send_notif_all()

# SmsSub
# EmailSub
# OthersSub
# SmsSub , new books = ['harry potter', 'lord of the ring']
# EmailSub , new books = ['harry potter', 'lord of the ring']
# OthersSub , new books = ['harry potter', 'lord of the ring']
# SmsSub
# EmailSub
# SmsSub , new books = ['magic']
# EmailSub , new books = ['magic']
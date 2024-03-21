class Mono:
    
    shared_state = {}
    
    def __init__(self) -> None:
        
        self.proccess = 12
        self.__dict__ = self.shared_state
    
        
x = Mono()
x.proccess = 18
y = Mono()
y.proccess = 55
print(x.__dict__)
print(y.__dict__)
print(x.proccess)
print(y.proccess)
# {'proccess': 55}
# {'proccess': 55}
# 55
55

# with __new__

class Mono:
    
    shared_state = {}
    
    def __new__(cls , *args , **kwargs):
        obj = super().__new__(cls,*args ,**kwargs)
        obj.__dict__ = obj.shared_state
        return obj
    
x = Mono()
x.proccess = 18
y = Mono()
y.proccess = 55
print(x.__dict__)
print(y.__dict__)
print(x.proccess)
print(y.proccess)
# {'proccess': 55}
# {'proccess': 55}
# 55
# 55
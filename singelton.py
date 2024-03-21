from typing import Any
class Singleton(object):
    
    class SingletonObject():
        
        def __init__(self):
            self.val = None
            
        def __str__(self) -> str:
            return "{0!r} <-> {1}".format(self , self.val)
        
    instance = None
    
    def __new__(cls):
        
        if not Singleton.instance:
            Singleton.instance = Singleton.SingletonObject()
            
        return Singleton.instance
            
    def __getattr__(self, __name: str) -> Any:
        return getattr(self.instance , __name)
        
    def __setattr__(self, __name: str) -> Any:
        return setattr(self.instance , __name)
        
        
s = Singleton()
s.val = "12"
print(s)
s2 = Singleton()
s2.val = "24"
print(s)
print(s2)

from typing import Any
from source.logs import Loggers


class Logger(object):
        
    def __init__(self , name) -> None:
        self.name = name
    
    instance = None
    
    def __new__(cls , name):
        
        if not Logger.instance:
            Logger.instance = Loggers(f"{__name__}.log")
            
            return Logger.instance
        
        else:
            return Logger.instance
            
    def __getattr__(self, __name: str) -> Any:
        return getattr(self.instance , __name)
        
    def __setattr__(self, __name: str) -> Any:
        return setattr(self.instance , __name)
        
        
logger = Logger("logs.log")
for i in range(15):
    logger.info(f"state new round {i + 1}")
    logger.warning(f"{i + 1}"*(i+1))
    logger.error(f"errorrrrrrrr")


# simple singleton 

class Singleton3:
    
    def __new__(cls):
        if not hasattr(cls , "instance"):
            cls.instance = super().__new__(cls)
            return cls.instance
        

# singleton with metaclass

class Singleton4(type):
    
    _instance = {}
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if not cls._instance.get(cls):
            cls._instance[cls] = super().__call__(*args , **kwds)
        return cls._instance[cls]
    
class Test_s4(metaclass = Singleton4):
    pass

l1 = Test_s4()
l2 = Test_s4()
print(l1 , l2)
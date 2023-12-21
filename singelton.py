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
        
        else:
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
# <__main__.Singleton.SingletonObject object at 0x000002103BE63D60> <-> 12
# <__main__.Singleton.SingletonObject object at 0x000002103BE63D60> <-> 24
# <__main__.Singleton.SingletonObject object at 0x000002103BE63D60> <-> 24

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


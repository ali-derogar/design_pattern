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



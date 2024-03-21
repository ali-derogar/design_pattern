from typing import Any


def printer():
    print("hello")
    
FirstClass = type("FirstClass" , (object,),{"printer":printer})
first = FirstClass()
first.printer


class MetaClassInt(type):
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print(f"args : {args}")
        return type.__call__(cls ,*args, **kwds)
    
class MyInt(metaclass = MetaClassInt):
    
    def __init__(self ,x,y) -> None:
        self.x=x
        self.y =y
        
x = MyInt(12,24)


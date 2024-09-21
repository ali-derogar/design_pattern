class Installation:
    def __init__(self ,source ,installation_path) -> None:
        self.source = source
        self.installation_path = installation_path
        self.choices = {}
    
    def preferences(self,command):
        self.choices.update(command)
        
    def execution(self):
        for key , choice in self.choices.items():
            if key == self.source and choice:
                print(key , "copyed to " , self.installation_path , end=" <::> ")
                print("success installition")
            else:
                print(key , "failed installition ! ")
    
i = Installation("python","D://new_folder")
i.preferences({"c#":False})
i.preferences({"python":True})
i.preferences({"java":False})
i.execution()

# c# failed installition !
# python copyed to  D://new_folder <::> success installition
# java failed installition !

class Recever:
    
    def __init__(self, action_) -> None:
        self.action_ = action_
        
    def action(self):
        print(type(self).__name__ , " : " , self.action_)
        
from abc import ABC , abstractmethod
class Command(ABC):
        
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    
    def __init__(self, recever) -> None:
        self.recever = recever
        
    def execute(self):
        return self.recever.action()
    
class Invoker:
    
    def __init__(self,commands) -> None:
        self.commands = commands
        
    def execute(self):
        for command in self.commands:
            command.execute()
        
r1 = Recever("voice check")
c1 = ConcreteCommand(r1)
r2 = Recever("network check")
c2 = ConcreteCommand(r2)
i = Invoker(commands=[c1 , c2])
i.execute()

# Recever  :  voice check
# Recever  :  network check

class HouseTrade:
    
    def buy(self) -> None:
        print(type(self).__name__ , " : khane kharide shode !")
        
    def sell(self) -> None:
        print(type(self).__name__ , " : khane frokhte shode !")
        
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Buy(Command):
    
    def __init__(self, recever) -> None:
        self.recever = recever
        
    def execute(self):
        return self.recever.buy()
    
class Sell(Command):
    
    def __init__(self, recever) -> None:
        self.recever = recever
        
    def execute(self):
        return self.recever.sell()
    
class Agent:
    
    def __init__(self,commands) -> None:
        self.commands = commands
        
    def execute(self):
        for command in self.commands:
            command.execute()
        
house_trader = HouseTrade()
c1 = Buy(house_trader)
c2 = Sell(house_trader)
i = Agent(commands=[c1 , c2])
i.execute()

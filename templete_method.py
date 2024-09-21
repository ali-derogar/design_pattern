from abc import ABCMeta , abstractmethod

class Compiler(metaclass = ABCMeta):
    
    @abstractmethod
    def CollectSourceCode(self):
        pass
    
    @abstractmethod
    def ComplieToObj(self):
        pass
    
    @abstractmethod
    def Run(self):
        pass
    
    # templete method
    def compile_run(self):
        self.CollectSourceCode()
        self.ComplieToObj()
        self.Run()
        print("compiling successfuly finished !")
        
class Android(Compiler):
    
    def CollectSourceCode(self):
        print("CollectSourceCode done :><:")
        
    def ComplieToObj(self):
        print("ComplieToObj done :><:")
        
    def Run(self):
        print("ComplieToObj done :><:")
        
class Client():
    
    def __init__(self,os) -> None:
        self.os = os
        
    def run(self):
        self.os.compile_run()
               
android = Android()
armin = Client(os=android)
armin.run()

# CollectSourceCode done :><:
# ComplieToObj done :><:
# ComplieToObj done :><:
# compiling successfuly finished !


class Safar(metaclass = ABCMeta):
    
    @abstractmethod
    def zaman_raft(self):
        pass
    
    @abstractmethod
    def roze_1(self):
        pass
    
    @abstractmethod
    def roze_2(self):
        pass
    
    @abstractmethod
    def zaman_bargasht(self):
        pass

    def run(self):
        self.zaman_raft()
        self.roze_1()
        self.roze_2()
        self.zaman_bargasht()
        
class Kish(Safar):
    
    def zaman_raft(self):
        print("zaman raft : 2 shanbe")
        
    def roze_1(self):
        print("shena dar daria")
        
    def roze_2(self):
        print("motor savari atraf jazire")
        
    def zaman_bargasht(self):
        return print("zaman bargasht : 4 shanbe")
    
class Gilan(Safar):
    
    def zaman_raft(self):
        print("zaman raft : 1 shanbe")
        
    def roze_1(self):
        print("shena dar rodkhane")
        
    def roze_2(self):
        print("koh navardi")
        
    def zaman_bargasht(self):
        return print("zaman bargasht : 3 shanbe")
    
class TeravelAgency:
    
    def make_choice(self):
        self.choice = input("which where do you want to go ? ").lower()
        self.check()
    
    def check(self):
        self.travel = None
        
        if self.choice == "kish":
            self.travel = Kish()
            
        if self.choice == "gilan":
            self.travel = Gilan()
            
        if not self.travel:
            print("your choice is not reachable")
            self.make_choice()
            
        else:
            self.travel.run()

t = TeravelAgency()
t.make_choice()

# which where do you want to go ? qom
# your choice is not reachable    
# which where do you want to go ? Gilan
# zaman raft : 1 shanbe
# shena dar rodkhane
# koh navardi
# zaman bargasht : 3 shanbe
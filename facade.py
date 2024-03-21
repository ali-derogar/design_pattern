
class EvantManager():
    
    def __init__(self):
        print("darhal barresi ba vahed hay marbote")
        
    def arreng(self):
        
        print("anjoman jam shodeh ast")
        
        self.theater_group =TheaterGroup()
        self.theater_group.set_theater_group()
        
        self.music_group = MuzicGroup()
        self.music_group.set_music_group()
        
        self.presentor = Presentor()
        self.presentor.set_presantation()
        
        self.lecture = Lecture()
        self.lecture.set_lectuer()
        
class TheaterGroup():
    
    def __init__(self) -> None:
        print("TheaterGroup hast komedi")
        
    def set_theater_group(self):
        print("grouh theater amade shodeh and")

class MuzicGroup():

    def __init__(self) -> None:
        print("MuzicGroup hast")
        
    def set_music_group(self):
        print(" MuzicGroup amade shodeh and")
        
class Presentor():
    
    def __init__(self) -> None:
        print("Presentor hast ")
        
    def set_presantation(self):
        print("Presentor amade shodeh and")

class Lecture():

    def __init__(self) -> None:
        print("Lecture hast ")
        
    def set_lectuer(self):
        print("lecture amade shodeh and")
        
class Manager():
    
    def __init__(self) -> None:
        print("kara ra angam dahid")
    
    def run(self):
    
        ev = EvantManager()
        ev.arreng()
    
if __name__ == "__main__":
    m = Manager()
    m.run()
    
# kara ra angam dahid
# darhal barresi ba vahed hay marbote
# anjoman jam shodeh ast
# TheaterGroup hast komedi
# grouh theater amade shodeh and   
# MuzicGroup hast
#  MuzicGroup amade shodeh and       
# Presentor hast 
# Presentor amade shodeh and
# Lecture hast 
# lecture amade shodeh and
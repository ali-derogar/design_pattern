from abc import ABC , abstractmethod
class Player:
    
    def __init__(self) -> None:
        self.has_contract = True
        
    def occupied(self):
        self.has_contract = True
        print(f"{type(self).__name__} has conttract and cant to join your team")
        
    def available(self):
        self.has_contract = False
        print(f"{type(self).__name__} is free and can join your team")
        
    def get_status(self):
        return self.has_contract
        
class Agent:
    
    def work(self):
        player = Player()
        if player.get_status():
            
            player.occupied()
        
        else:
            
            player.available()
        
    
if __name__ == "__main__":
    a = Agent()
    a.work()
    
    
class PardakhtKardan(ABC):
    @abstractmethod
    def do_pay(self):
        pass
    
class Bank(PardakhtKardan):
    
    def __init__(self) -> None:
        self.account = None
        self.card = None
        
    def _get_account(self):
        self.account = self.card
        return self.account
    
    def _mojodi_hesab(self):
        print(f"Bank check mikonad ke aya {self._get_account()} be andaze kafi mojodi dard")
        return True
    
    def set_card(self,card):
        self.card = card
        
    def do_pay(self):
        if self._mojodi_hesab():
            print("bank : hazine pardakht shod")
            return True
            
        else:
            print("mojodi kafi nist")
            return False

class Card(PardakhtKardan):
    
    def __init__(self) -> None:
        self.bank = Bank()
        
    def do_pay(self):
        self.card = input("card khod ra vared konid")
        self.bank.set_card(card=self.card)
        return self.bank.do_pay()
    
class You:
    
    def __init__(self) -> None:
        print("i wanna to buy a shirts")
        self.card = Card()
        self.is_purchased = None
        
    def pardakht(self):
        
        self.is_purchased = self.card.do_pay()
        
    def __del__(self):
        
        if self.is_purchased:
            print("pardakht anjam shod")
        else:
            print("mojodi kafi nist")
            
if __name__ == "__main__":
    y = You()
    y.pardakht()
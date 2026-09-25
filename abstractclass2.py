from abc import ABC ,abstractmethod
class atm(ABC):
    @abstractmethod
    def authenticateuser(self,cardno,pin):
        pass
    @abstractmethod
    def withdrawcash(self,cash):
        pass
    @abstractmethod
    def depositcash(self,cash):
        pass

class bankatm(atm):
    def __init__(self):
        self.balance=10000
    def authenticateuser(self,cardno,pin):
        print(f"the card no is {cardno},having pin no {pin}")
        return True
    def withdrawcash(self, cash):
        if cash <=self.balance:
            self.balance -=cash
            print(f"you have withdraw amount of {cash}")
        else:
            print("insufficient balance")
    def depositcash(self, cash):
        self.balance+=cash
        print(f"deposited blance is {cash}")
        print(f"avalible blance is {self.balance}")
#creating object
user1=bankatm()
if user1.authenticateuser("12345",8006):
        user1.withdrawcash(2000)
        user1.depositcash(5000)
        
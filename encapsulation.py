class bankaccount:
    def __init__ (self):#private constructor
        self.balance=200

    def deposit(self,ammount):#method
        self.balance+=ammount

    def withdraw(self):
        return self.balance

#object of the class
bank=bankaccount()
bank.deposit(5000)
print(f"the account balance is {bank.withdraw()}")
class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            print(f"the deposit amount:{amount}and total balance:{self.balance}")
    def withdraw(self,amount1):
        if 0<amount1<=self.balance:
            self.balance-=amount1
            print(f"the withdraw amount:{amount1}and total balance:{self.balance}")
        else:
            print("insufficient balance")

acc=bankaccount(500)
acc.deposit(3000)
acc.withdraw(200)

        
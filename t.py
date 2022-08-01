class BankAccount:
    interest_rate=4.0
    def __init__(self,fname,lname,amount):
        self.balance=float(amount)
        self.fname=fname
        self.lname=lname
        self._transaction=[]
        self._transaction.append(f"initial deposit {amount}")
       
    def withdraw(self,amount):
        self.balance-=float(amount)
        self._transaction.append(f"withdrawl amount {amount}")
    def deposit(self,amount):
        self.balance+=float(amount)
        self._transaction.append(f"deposited amount {amount}")
    def statement(self):
        for line in self._transaction:
            print(line)
        print(f"total balance {self.balance}")
    
    def roi(self):
        self.balance+=self.balance*(BankAccount.interest_rate/10)

class SavingsAccount(BankAccount):
    def __init__(self,fname,lname,amount):
        super().__init__(fname,lname,amount)
    def withdraw(self,amount):
        if amount>2000:
            raise Exception("Balance is less")
        super().withdraw(amount)
##sa=SavingsAccount('siri','s',1000)

class SalaryAccount(SavingsAccount):
    def __init__(self,fname,lname,amount):
        super().__init__(fname,lname,amount)
    def withdraw(self,amount):
        if amount>self.balance:
            raise Exception("Withdraw amount is more")
        super().withdraw(amount)

##sa=SalaryAccount('shalini','s',5000)
class PenaltyAccount(BankAccount,SavingsAccount):  










        

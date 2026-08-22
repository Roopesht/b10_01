class Account:
    bank_balance = 0
    def __init__(self, acname, balance):
        self.name = acname
        self.balance = balance
        Account.bank_balance += balance
    def deposit(self, amount):
        self.balance += amount
        Account.bank_balance += amount
    def withdrawl(self, amount):
        if self.balance < amount:
            print ("No sufficient balance")
            return
        self.balance -= amount
        Account.bank_balance -= amount
    def print_info(self):
        print (f"name: {self.name}, Balance: {self.balance}, Bank Balance: {Account.bank_balance}")
    def print_bank_balance():
        print ("Bank Balance: ", Account.bank_balance)

class CurrentAccount (Account):
    def __init__(self, acname, balance, od_limit):
        super().__init__(acname, balance)
        self.od_limit = od_limit
        pass
    def withdrawl(self, amount):
        if self.balance + self.od_limit < amount:
            print ("No sufficient balance")
            return
        self.balance = self.balance - amount

roopesh_cu_ac = CurrentAccount("Roopesh", 5000, 10000)
roopesh_cu_ac.print_info()
roopesh_cu_ac.withdrawl(11000)
roopesh_cu_ac.print_info()
roopesh_cu_ac.withdrawl(4000)
roopesh_cu_ac.print_info()
roopesh_cu_ac.withdrawl(1000)

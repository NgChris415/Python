class BankAccount:
    def __init__(self, int_rate = 1.05, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = (self.balance + amount)
        print(self.balance)
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough balance")
        else:
            self.balance = (self.balance - amount)
        print(self.balance)
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate)
        print(self.balance)
        return self

account1 = BankAccount(1.05, 1000)
account2= BankAccount(1.045, 500)

account1.deposit(150).deposit(500).deposit(25).yield_interest().display_account_info()
account2.deposit(50).deposit(1000).withdraw(20).withdraw(100).withdraw(50).withdraw(50).yield_interest().display_account_info()
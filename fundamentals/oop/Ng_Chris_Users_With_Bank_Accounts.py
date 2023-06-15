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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_account(self):
        print(self.account.display_account_info)

chris = User("Chris Ng", "ngchris123@hotmail.com")
ela = User("Ela Tedjokusumo", "BerryBug@gmail.com")


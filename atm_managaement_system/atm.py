class Atm:
    def __init__(self, holname, pin, accno, bankname, balance=1000):
        self.holname = holname
        self.pin = pin
        self.accno = accno
        self.bankname = bankname
        self.balance = balance

    def details(self):
        print("Holder Name:", self.holname)
        print("Account Number:", self.accno)
        print("Bank Name:", self.bankname)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited Successfully")
        print("Total Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdraw Successful")
            print("Total Balance:", self.balance)

    def check_balance(self):
        print("Available Balance:", self.balance)

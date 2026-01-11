from atm import Atm
from storage import load_accounts, save_accounts

accounts = load_accounts()

if not accounts:
    accounts[122232] = Atm("ramu", 3699, 122232, "Andhra Bank")

pin = int(input("Enter PIN: "))
acc = accounts[122232]

if pin != acc.pin:
    print("Incorrect PIN")
else:
    while True:
        print("\n1.Account Details\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            acc.details()

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            acc.deposit(amount)
            save_accounts(accounts)

        elif choice == 3:
            amount = int(input("Enter withdraw amount: "))
            acc.withdraw(amount)
            save_accounts(accounts)

        elif choice == 4:
            acc.check_balance()

        elif choice == 5:
            save_accounts(accounts)
            break

        else:
            print("Invalid choice")

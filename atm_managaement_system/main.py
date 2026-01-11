from atm import Atm
from storage import load_accounts, save_accounts

accounts = load_accounts()

if not accounts:
    print("No accounts found. Creating default account...")
    acc = Atm("Ramu", 3699, 122232, "Andhra Bank", 1000)
    accounts[acc.accno] = acc
    save_accounts(accounts)


accno = int(input("Enter account number: "))

if accno not in accounts:
    print("Account not found")
    exit()

atm = accounts[accno]

pin = int(input("Enter pin: "))
if pin != atm.pin:
    print("Incorrect pin")
    exit()
    
while True:
    print("\n1.Account details\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        atm.details()

    elif ch == 2:
        atm.deposit()
        save_accounts(accounts)

    elif ch == 3:
        atm.withdraw()
        save_accounts(accounts)

    elif ch == 4:
        atm.checkbalance()

    elif ch == 5:
        save_accounts(accounts)
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")

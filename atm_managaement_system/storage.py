import json
from atm import Atm

FILE_NAME = "accounts.json"


def load_accounts():
    try:
        file = open(FILE_NAME, "r")
        data = json.load(file)
        file.close()

        accounts = {}
        for accno in data:
            acc = data[accno]
            accounts[int(accno)] = Atm(
                acc["holname"],
                acc["pin"],
                int(accno),
                acc["bankname"],
                acc["balance"]
            )
        return accounts

    except FileNotFoundError:
        return {}


def save_accounts(accounts):
    data = {}

    for accno in accounts:
        acc = accounts[accno]
        data[accno] = {
            "holname": acc.holname,
            "pin": acc.pin,
            "bankname": acc.bankname,
            "balance": acc.balance
        }

    file = open(FILE_NAME, "w")
    json.dump(data, file)
    file.close()

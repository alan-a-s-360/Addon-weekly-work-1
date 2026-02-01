#simple bank applicatoin 3
def deposit(d_amount):
    balance=0
    balance+=d_amount
    return balance

def withdraw(w_amount,balance):
    if balance>=w_amount:
        return balance-w_amount
    else:
        print("No balance")

def check_balance():
    d_amount=float(input("Enter the amount you deposit= "))
    w_amount=float(input("Enter the amount you withdraw= "))
    balance=deposit(d_amount)
    total=withdraw(w_amount,balance)
    print("Balance amount in your bank= ",total)

check_balance()


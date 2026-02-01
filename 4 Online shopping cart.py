#online shopping cart 4
cart={}
def add_items():
    n=int(input("Enter how many items add= "))
    for i in range(1,n+1):

        name=input(f"Enter the name of item {i}= ")
        price=int(input(f"Enter the price of item {i}= "))
        cart[name]=price

def remove_items():
    n=int(input("Enter how many items remove= "))
    for i in range(1,n+1):
        name=input(f"Enter the removed item {i}= ")
        if name in cart:
            del cart[name]
        else:
            pass
    return cart

def total(cart):
    total=sum(cart.values())
    print("Total amount= ",total)
    return total

def discount(total):
    dis=int(input("Enter the discount(%)= "))
    amount=total-((dis*total)/100)
    print("Final amount= ",amount)

add_items()
cart=remove_items()
total=total(cart)
discount(total)

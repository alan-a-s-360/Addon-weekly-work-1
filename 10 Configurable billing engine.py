# configurable billing engine 10
def calculate_bill(amount, tax_function):
    tax = tax_function(amount)
    total = amount + tax
    return total


# Different tax rules (can be extended easily)
def india_tax(amount):
    return amount * 0.18


def usa_tax(amount):
    return amount * 0.10


def eu_tax(amount):
    return amount * 0.20



amount = input("Enter your amount= ")

print("India Bill:", calculate_bill(amount, india_tax))
print("USA Bill:", calculate_bill(amount, usa_tax))
print("EU Bill:", calculate_bill(amount, eu_tax))

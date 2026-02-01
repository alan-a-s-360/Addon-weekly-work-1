#electricity bill calculation 6
def unit_consumed():
    unit=int(input("Enter unit consumed= "))
    return unit

def calculate_bill(unit):
    if unit<=100:
        bill=unit*2
    elif 100<unit<=300:
        bill=(100*2)+(unit-100)*3
    else:
        bill=(100*2)+(200*3)+(unit-300)*5
    return bill

def generate_bill(unit,bill):
    print("\n------Electricity Bill--------")
    print("Unit consumed= ",unit)
    print("Total bill amount= ",bill)

unit=unit_consumed()
bill=calculate_bill(unit)
generate_bill(unit,bill)

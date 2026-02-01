#employee salary calculator 1
def employee_details():
    print("-----Employee details-----")
    print("   ")
    name=input("Enter name= ")
    basic=float(input("Enter basic salary= "))
    hra=float(input("Enter HRA= "))
    da=float(input("Enter DA= "))
    return name,basic,hra,da

def gross_salary(basic,hra,da):
    return basic+hra+da

def calculate_deduction(gross):
    return gross*0.10

def display_salary(name,gross,deduction):
    net=gross-deduction
    print(" ")
    print("-----Salary-----")
    print(" ")
    print("Employee= ",name)
    print("Gross Salary= ",gross)
    print("Deduction= ",deduction)
    print("Net Salary= ",net)

name,basic,hra,da = employee_details()
gross=gross_salary(basic,hra,da)
deduction=calculate_deduction(gross)
display_salary(name,gross,deduction)

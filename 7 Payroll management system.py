#payroll management system 7
def employee_data():
    print("*------Employee Details------*")
    print(" ")
    name=input("Enter name= ")
    emp_id=int(input("Enter id number= "))
    basic=float(input("Enter basic salary/day= "))
    day=int(input("Enter how day in this month= "))
    hra=float(input("Enter HRA= "))
    da=float(input("Enter DA= "))
    deduction=float(input("Enter deduction= "))
    return name,emp_id,basic,day,hra,da,deduction

def calculate_salary(basic,day):
    basic_salary=basic*day
    return basic_salary

def bouns_deduction(basic_salary,hra,da,deduction):
    salary=basic_salary+hra+da-deduction
    return salary

def pyroll_report(salary,basic_salary):
    print("*------Salary Details------*")
    print(" ")
    print("actual salary= ",basic_salary)
    print("Net salary= ",salary)

name,emp_id,basic,day,hra,da,deduction=employee_data()
basic_salary=calculate_salary(basic,day)
salary=bouns_deduction(basic_salary,hra,da,deduction)
print(" ")
pyroll_report(salary,basic_salary)

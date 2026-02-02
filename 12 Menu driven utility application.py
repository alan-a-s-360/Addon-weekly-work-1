# menu driven utility application 12
def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", a / b if b != 0 else "Not possible")


def string_operations():
    s = input("Enter a string: ")
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    print("Reversed:", s[::-1])
    print("Length:", len(s))


def number_utilities():
    n = int(input("Enter a number: "))
    print("Square:", n * n)
    print("Even" if n % 2 == 0 else "Odd")


def menu():
    while True:
        print("\n1. Calculator")
        print("2. String Operations")
        print("3. Number Utilities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            string_operations()
        elif choice == "3":
            number_utilities()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


menu()

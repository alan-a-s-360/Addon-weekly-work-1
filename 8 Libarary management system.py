# library management system 8
books=[]
def add_book():
    n=int(input("Enter number of books add= "))
    for i in range(1,n+1):
        name=str(input(f"Enter name of book {i}= "))
        books.append(name)
    return books

def issue_book():
    n=int(input("Enter number of book issue= "))
    for i in range(1,n+1):
        name=str(input("Enter name of issue book= "))
        if name in books:
            books.remove(name)
        else:
            print("That book is not available")
    return books

def return_book():
    name=str(input("Enter the book return= "))
    books.append(name)
    return books

def search_book():
    name=str(input("Enter book to search= "))
    print("Avialable books =",books)
    if name in books:
        print(name," is available")
    else:
        print(name," is not available")

books=add_book()
books=issue_book()
books=return_book()
search_book()

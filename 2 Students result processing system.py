#students result processing system 2
def subject_mark():
    subject=int(input("Enter number of subject= "))
    total=0
    for i in range(1,subject+1):
        mark=float(input(f"Enter the mark of subject {i}= "))
        total+=mark
    return total,subject,mark

def total_average(total):
    average=total/subject
    print("Total= ",total)
    print("Average= ",average)
    return average

def grade(average):
    if 40>=average>30:
        grade="A"
    elif 30>=average>20:
        grade="B"
    elif 20>=average>=10:
        grade="C"
    elif 10>average:
        grade="fail"
    else:
        grade="Not defined"
    print("Grade= ",grade)

def display():
    total,subject,mark=subject_mark()
    average=total_average(total)
    grade(average)

display()

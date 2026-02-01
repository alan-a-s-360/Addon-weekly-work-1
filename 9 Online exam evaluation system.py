# online exame evaluation system 9
student_answer=[]
correct_answer=[]
def validate_answer():
    print("*------Answer------*")
    print(" ")
    n=10
    print("Number of questions= ",n)
    print("*--Option are (A,B,C,D)--*")
    for i in range(1,n+1):
        student=input(f"Enter the answer of student (Q.no{i})= ")
        student_answer.append(student)
    
    for j in range(1,n+1):
        correct=input(f"Enter the correct answer (Q.no{j})= ")
        correct_answer.append(correct)
    return n,student_answer,correct_answer

def calculate_score(n,student_answer,correct_answer):
    score=0
    for i in range(0,n):
        if student_answer[i]==correct_answer[i]:
            score+=1
        else:
            pass
    return score

def generate_grade(score):
    if 10>=score>8:
        grade="A"
    elif 8>=score>6:
        grade="B"
    elif 6>=score>4:
        grade="C"
    else:
        grade="fail"
    print(" ")
    print("*---Students Mark And Grade---*")
    print(" ")
    print(f"Mark of student is {score} and grade is {grade}")

n,student_answer,correct_answer=validate_answer()
score=calculate_score(n,student_answer,correct_answer)
generate_grade(score)

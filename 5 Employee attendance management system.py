#employee attendance management system 5
def mark_attendance():
    days=int(input("Enter total days in a month= "))
    P=0
    A=0
    N=0
    for i in range(1,days+1):
        attendance=input(f"Enter present/absent/not working day(P/A/N) at day {i}= ")
        if attendance=="P":
            P+=1
        elif attendance=="A":
            A+=1
        elif attendance=="N":
            N+=1
    return P,A,N

def working_days(P,A):
    return P+A

def attendance_report(working,P,A,N):
    print("Working days= ",working)
    print("Present days= ",P)
    print("Absent days= ",A)
    print("Not woking day= ",N)

P,A,N=mark_attendance()
working=working_days(P,A)
attendance_report(working,P,A,N)

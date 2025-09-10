#-Write a Python program to calculate grades based on percentage...


s1=int(input("enter subject1 mark:"))
s2=int(input("enter subject2 mark:"))
s3=int(input("enter subject3 mark:"))
s4=int(input("enter subject4 mark:"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40:

    total=s1+s2+s3+s4
    print("total is:",total)

    pr=total/4
    print("preercentage is:",pr)

    if pr>=90:
        print("grade:A+")
    elif pr>=80:
        print("grade:A")
    elif pr>=70:
        print("grade:B+")
    elif pr>=60:
        print("grade:B")
    elif pr>=50:
        print("grade:C")
    elif pr>=40:
        print("grade:D")

else:
    print("the student is FAIL")
    
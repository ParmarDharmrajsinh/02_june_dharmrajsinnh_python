s1=int(input("enter subject1 mark"))
s2=int(input("enter subject2 mark"))
s3=int(input("enter subject3 mark"))
s4=int(input("enter subject4 mark"))

total=s1+s2+s3+s4
print("total:",total)

pr=total/4
print("PR:",pr)

if pr>=70:
    print("dist. ")

elif pr>=60:
    print("first class")
elif pr>=50:
    print("second class")
else:
    print("pass class")
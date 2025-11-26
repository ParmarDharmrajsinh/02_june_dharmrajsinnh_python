#write a python program to check if a number is prime using  if_else...
i=1
no=int(input("enter the number:"))
while i<=no:
    i+=1

    if no%i==0:
        print("number is not prime")
        break
    else:
        print("number is prime")
        break
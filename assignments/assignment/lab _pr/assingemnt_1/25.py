#Write a Python program to stop the loop once 'banana' is found using the break statement. 


list1=['apple','banana','mango','orange']

for fruit in list1:
    if fruit=='banana':
        print("'banana found stopping the loop.")

        break# exit the loopp 

    print(fruit)
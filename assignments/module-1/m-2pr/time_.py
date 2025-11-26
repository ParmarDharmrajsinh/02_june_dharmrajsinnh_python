import random
import datetime
x=open("stdata.txt","w")
choice=int(input("how many student "))



for i in range(choice):
    id=input("enter an id:")
    x=str(id)
    name=input("enter a name:")
    city=input("enter a city:")


    x.write("created at:",+str(datetime.datetime.now*()+"\n"))

    
    x.id=("id:",id)
    x.name=(" name:",name)
    x.city=("city:",city)

    

    
print(x)

dict={}

n = int(input("enter number of pairs:"))

for i in range(n):
    x = input("Enter your key's:")
    u= input("Enter your value's:")

    dict[x]=u
print(dict)


for i in range(len(keys)):
    v=input(f"enter value of {keys[i]}:")
    dict=[keys][i]=v
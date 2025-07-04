import pandas
import requests

url="https://api.escuelajs.co/api/v1/products"

req=requests.get(url)
data=req.json()
total=0

p=pandas.DataFrame(data)[["id","title","price"]]


for i in data:
    total += i['price']


print(p)
print("total price of all product:",total)
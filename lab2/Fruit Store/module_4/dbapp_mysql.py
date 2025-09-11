import pymysql

try:
    db=pymysql.connect(host="127.0.0.1",user="root",password="",
    database="pydb")
    print("database connected")
except Exception as e:
    print(e)

# table create 

tbl_create="create table studinfo(id integer primary key autoincrement,name text,city  text"
cr=db.cursor()
try:
    cr.execute(tbl_create)
    print("table created")
except Exception as e:
    print(e)

#insert data
insert_data="insert into studinfo(name,city) values(%s,%s)"
try:
    cr.execute(insert_data)
    db.commit()
    print("record inserted")
except Exception as e:
    print(e)



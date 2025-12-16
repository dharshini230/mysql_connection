from tabulate import tabulate
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="2005",database="python_db")
if con:
    print("Connection successful")
else:
    print("Connection failed")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users (name,age,city) values (%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data Inserted successsfully")
def update(id,name,age,city):
    res = con.cursor()
    sql = "update  users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print("Data update successsfully")


def select():
    res=con.cursor()
    sql="select ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data deleted successsfully")


while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        city=input("Enter your city:")
        insert(name,age,city)

    elif choice == 2:
        id=int(input("Enter your id:"))
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        city = input("Enter your city:")
        update(name, age, city)
    elif choice == 3:
        select()
    elif choice == 4:
        id=int(input("Enter your id:"))
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Enter a valid choice")







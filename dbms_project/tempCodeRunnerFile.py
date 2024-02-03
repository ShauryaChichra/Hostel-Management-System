import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
mycursor=mydb.cursor()
mycursor.execute("Select*from mytable")

for x in mycursor:
    print(x)
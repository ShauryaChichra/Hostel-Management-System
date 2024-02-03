import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
mycursor=mydb.cursor()
mycursor.execute("Select*from mytable")
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)
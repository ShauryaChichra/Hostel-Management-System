import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
mycursor=mydb.cursor()
mycursor.execute("Select*from mytable")
myrecords=mycursor.fetchall()

detail = myrecords[random.randint(1, 1000)]
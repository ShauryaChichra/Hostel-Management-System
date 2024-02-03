import mysql.connector
import random

def inf(roll):
     #sample(input from user)
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
    mycursor=mydb.cursor()
    query="Select * from mytable where rollno="+str(roll)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    
    return myrecords

def hostel(roll):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
    mycursor=mydb.cursor()
    query="Select * from hostelalloted where rollno="+str(roll)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    
    return myrecords
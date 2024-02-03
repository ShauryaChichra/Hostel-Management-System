import mysql.connector
import random

def allot(roll):
     #sample(input from user)
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
    mycursor=mydb.cursor()
    query="Select hostel from hostelalloted where rollno="+str(roll)
    print(query)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    hostelalloted=myrecords[0][0]
    query="Select room from "+myrecords[0][0]+" where roll_no is NULL"
    print(query)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    list=[];
    
    for x in myrecords:
        list.append(x)
    return list
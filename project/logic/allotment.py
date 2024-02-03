import mysql.connector
import random

def allot(roll):
     #sample(input from user)
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")
    mycursor=mydb.cursor()
    query="Select hostel from hostelalloted where rollno="+str(roll)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    hostelalloted=myrecords[0][0] #alloted hostel
    query="Select room from "+hostelalloted+" where roll_no is NULL"
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    list=[]
    for x in myrecords:
        list.append(x[0])
    return list
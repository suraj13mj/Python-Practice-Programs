

#Connection to Backend MySQL

import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb
db = MySQLdb.connect("localhost","root","","tkinter_student")
cur = db.cursor()



#Functions to perform CRUD operations in Backend MySQL

from Bean_Student import *

def insertStudent(stud):
    sql = "INSERT INTO student VALUES ('"+stud.Name+"',"+str(stud.Rollno)+",'"+stud.Address+"','"+stud.College+"','"+stud.Branch+"','"+stud.Sex+"',"+str(stud.News)+")"                                
    cur.execute(sql)
    db.commit()
    return True

def checkPassword(stud):
 	sql = "SELECT * FROM registration WHERE username='"+stud.Username+"' and password='"+stud.Password+"'"
 	cur.execute(sql)
 	rows = cur.fetchall()
 	db.commit()
 	return rows

def insertLoginDetails(stud):
    sql = "INSERT INTO registration VALUES ('"+stud.Username+"','"+stud.Password+"')"                                
    cur.execute(sql)
    db.commit()
    return True



"""
if __name__ == "__main__":
    stud = Student("Amit",1001,"Vidynagar,Hubli","BVB","CSE","MALE",1)
    insertStudent(stud)
"""

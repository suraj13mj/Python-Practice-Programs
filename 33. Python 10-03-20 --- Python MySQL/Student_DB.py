import Student

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db=MySQLdb.connect("localhost","root","","stud_db")


def insertStudent(s):
	cur=db.cursor()
	sql="INSERT INTO student VALUES("+str(s.rollno)+",'"+s.name+"',"+str(s.per)+")"
	cur.execute(sql)
	db.commit()


def updateStudent(s):
	cur=db.cursor()
	sql="UPDATE student SET name='"+str(s.name)+"',percentage="+str(s.per)+" WHERE rollno="+str(s.rollno)
	cur.execute(sql)
	db.commit()


def deleteStudent(rollno):
	cur=db.cursor()
	sql="DELETE FROM student WHERE rollno="+str(rollno)
	cur.execute(sql)
	db.commit()
	print("1 record deleted")


def fetchStudents():
	cur=db.cursor()
	sql="SELECT * FROM student"

	cur.execute(sql)
	rows=cur.fetchall()
	lst=[]
	for s in rows:
		stud=Student.Student(s[0],s[1],s[2])
		lst.append(s)
	return lst


def searchStudent(rollno):
	cur=db.cursor()
	sql="SELECT * FROM student WHERE rollno="+str(rollno)

	cur.execute(sql)
	rows=cur.fetchall()
	lst=[]
	for s in rows:
		stud=Student.Student(s[0],s[1],s[2])
		lst.append(s)

	if len(lst)==0:
		return None
	else:
		return lst


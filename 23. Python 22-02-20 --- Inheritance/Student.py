"""
Program to demonstrate Inheritance in Python with Student as Superclass and Marks as Subclass
Single Inheritance
 
					Student
					   ^
					   |
		               |
		             Marks  
"""

class Student:
	def __init__(self,rollno=0,name=" "):
		self.__rollno=rollno
		self.__name=name

	def readStudent(self):
		self.__rollno=int(input("Enter Student RollNo:"))
		self.__name=input("Enter Student Name:")

	def displayStudent(self):
		print("\nRollNo:"+str(self.__rollno),"Name:"+self.__name,sep="\n")



""" ----------------------------------------------------------------- """ 



class Student:
	def __init__(self,rollno=0,name="",per=0.0):
		self.rollno=rollno
		self.name=name
		self.per=per

	def readStudent(self):
		self.rollno=int(input("Enter Student Rollno:"))
		self.name=input("Enter Student Name:")
		self.per=float(input("Enter Percentage:"))

	def __str__(self):
		st="Rollno:"+str(self.rollno)+"Name:"+self.name+"Percentage:"+str(self.per)
		return st

	def displayStudent(self):
		print(self)
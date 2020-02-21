# Program to define a class Student and read a Student record and display it

class Student:
	def __init__(self,roll=0,name='',addr=''):
		self.roll=roll
		self.name=name
		self.addr=addr

	def readStudent(self):
		self.roll=int(input("Enter Student Roll No:"))
		self.name=input("Enter Student Name:")
		self.addr=input("Enter Student Address:")

	def displayStudnet(self):
		print("ROLL NO:"+str(self.roll),"NAME:"+str(self.name),"ADDRESS:"+str(self.addr),sep='\n')


s1=Student(101,"Anil","Hubli")
s1.displayStudnet()

s2=Student()
s2.readStudent()
s2.displayStudnet()
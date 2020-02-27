""" 
Program to demonstrate Diamond Problem in Inheritance 
Hybrid Inheritance : Multiple Inheritance + Hierarchial Inheritance

					Student
					   ^
		   ____________|______________
		  |							  |
		Marks					   Sports
		  |___________________________|
					   |
		             Result

"""

class Student:
	def __init__(self,rollno=0,name=" "):
		self.rollno=rollno
		self.name=name

	def read(self):
		self.rollno=int(input("Enter Student RollNo:"))
		self.name=input("Enter Student Name:")

	def display(self):
		print("\nRollNo:"+str(self.rollno),"Name:"+self.name,sep="\n")



""" ----------------------------------------------------------------- """ 


class Marks(Student):
	def __init__(self,rollno=0,name=" ",marks1=0,marks2=0):
		super().__init__(rollno,name)
		self.marks1=marks1
		self.marks2=marks2

	def read(self):
		super().read()
		self.marks1=int(input("Enter Marks1:"))
		self.marks2=int(input("Enter Marks2:"))

	def display(self):
		super().display()
		print("Marks1:"+str(self.marks1),"Marks2:"+str(self.marks2),sep="\n")


""" ----------------------------------------------------------------- """ 

class Sports(Student):
	def __init__(self,sgrade=0):
		self.sgrade=sgrade                             				#Here we don't call Student class __init__() ; read() ; display()
													   				#because it overwrites same data read by Marks class
													   				#Diamond Problem
	def read(self):
		self.sgrade=int(input("Enter Sports grade:"))

	def display(self):
		print("Sports grade:"+str(self.sgrade))



""" ----------------------------------------------------------------- """

class Result(Marks,Sports):														#Multiple Inheritance
	def __init__(self,rollno=0,name=" ",marks1=0,marks2=0,sgrade=0):          
		Marks.__init__(self,rollno,name,marks1,marks2)
		Sports.__init__(self,sgrade)
		self.total=marks1+marks2
		self.per=self.total/2

	def read(self):
		Marks.read(self)
		Sports.read(self)
		self.total=self.marks1+self.marks2
		self.per=self.total/2

	def display(self):
		Marks.display(self)
		Sports.display(self)
		print("Total:"+str(self.total),"Percentage:"+str(self.per))



if __name__=="__main__":
	N=int(input("Enter the No of Students:"))
	stud=[]
	for i in range(0,N):
		print("1")
		s=Result()
		s.read()
		stud.append(s)

	for x in stud:
		x.display()

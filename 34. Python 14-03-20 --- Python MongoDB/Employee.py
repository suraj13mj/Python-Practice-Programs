class Employee:
	def __init__(self,eno=0,name=' ',salary=0):
		self.eno=eno
		self.name=name
		self.salary=salary

	def readEmployee(self):
		self.eno=int(input("Enter Employee Number:"))
		self.name=input("Enter Employee Name:")
		self.salary=int(input("Enter Employee salary:"))

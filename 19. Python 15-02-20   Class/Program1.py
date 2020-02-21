#Program to define a class Employee, to read and display an Employee record


class Employee:
	def __init__(self,Eno=0,Ename='',Basic=0):
		self.Empno=Eno
		self.Empname=Ename
		self.Basic=Basic
		self.calcSalary()

	def readEmployee(self):
		self.Empno=int(input("Enter Employee Number:"))
		self.Empname=input("Enter Name:")
		self.Basic=int(input("Enter Basic Salary:"))
		self.calcSalary()

	def readEmployee(self):
		self.Empno=int(input("Enter Employee Number:"))
		self.Empname=input("Enter Name:")
		self.Basic=int(input("Enter Basic Salary:"))
		self.calcSalary()

	def calcSalary(self):
		self.hra=self.Basic*0.10
		self.da=self.Basic*0.73
		self.gross=self.Basic+self.hra+self.da
		self.tax=0.3*self.gross
		self.net=self.gross-self.tax

	def displayEmployee(self):
		print("Empno:"+str(self.Empno),"Name:"+str(self.Empname),"Basic Salary:"+str(self.Basic),"HRA:"+str(self.hra),"DA:"+str(self.da),"Gross Salary:"+str(self.gross),"Income Tax:"+str(self.tax),"Net Salary:"+str(self.net),sep='\n')


e1=Employee(101,"Anil",10000)
e1.displayEmployee()


e2=Employee()
e2.readEmployee()
e2.displayEmployee()

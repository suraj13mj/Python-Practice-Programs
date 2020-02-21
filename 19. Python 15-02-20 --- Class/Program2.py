# Program to define a class Employee, read N employee records and display the same.


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

emp=[]

N=int(input("Enter the Number of Employees:"))
for i in range(0,N):
	e=Employee()
	e.readEmployee()
	emp.append(e)

for x in emp:
	x.displayEmployee()
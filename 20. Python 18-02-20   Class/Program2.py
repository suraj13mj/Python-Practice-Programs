#Program to read Employee details such that EmpNo is automatically generated from 1001 using class attributes

class Employee:
	empno=1001
	def __init__(self,name='',salary=0):
		self.empname=name
		self.empsalary=salary
		Employee.empno+=1

	def readEmployee(self):
		self.empname=input('Enter Employee Name:')
		self.empsalary=int(input('Enter Employee salary:'))

	def displayEmployee(self,eno):
		print("EmpNo:"+str(eno),"Name:"+str(self.empname),"Salary:"+str(self.empsalary),end='\n\n')


emp={}
while True:
	ch=int(input("1.New Employee\n2.Display Employee\n3.Exit\n"))
	if ch==1:
		e=Employee()
		e.readEmployee()
		emp[Employee.empno-1]=e

	elif ch==2:
		for eno in emp.keys():
			emp[eno].displayEmployee(eno)

	elif ch==3:
		break
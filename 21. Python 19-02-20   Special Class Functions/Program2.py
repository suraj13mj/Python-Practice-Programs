#Demonstrate the working of the special functions __gt__ and __lt__ 
#Operator Overloading of > and <

class Employee:
	empno=1001
	def __init__(self,name='',salary=0):
		self.empno=Employee.empno
		self.empname=name
		self.empsalary=salary
		Employee.empno+=1

	def readEmployee(self):
		self.empname=input('Enter Employee Name:')
		self.empsalary=int(input('Enter Employee salary:'))


	def __gt__(self,x):
		print("Method __gt__ called")
		if self.empsalary > x.empsalary:
			return True

	def __lt__(self,x):
		print("Method __lt__ called")
		if self.empsalary < x.empsalary:
			return True


if __name__=="__main__":

	e1=Employee()
	e1.readEmployee()

	e2=Employee()
	e2.readEmployee()

	if e1 > e2:
		print("Employee 1 salary is greater")
	elif e1 < e2:
		print("Employee 2 salary is greater")


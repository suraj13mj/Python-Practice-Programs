#Demonstrate the working of the special function __str__ to display objects

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

	
	def __str__(self):																						#Over-riding Object class __str__ method
		s=""+"\nEmpNo:"+str(self.empno)+"\nName:"+self.empname+"\nSalary:"+str(self.empsalary)+"\n"       
		return(s)
    
    


emp=[]       #List
N=int(input("Enter the No of Employees:"))
for i in range (0,N):
	e=Employee()
	e.readEmployee()
	emp.append(e)

for x in emp:
	print(x)

      #OR

for x in emp:
	a=""+str(x)
	print(a)




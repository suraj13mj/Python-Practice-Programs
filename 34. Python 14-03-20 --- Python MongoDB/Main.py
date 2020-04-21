#Program to demonstrate how to use MongoDB with Python

import Employee
import Emp_MongoDB

while True:
	ch=int(input("\n1->New Employee  2->Delete Employee  3->Update Employee  4->Search Employee  5->Display Employees  6->Exit\n"))
	if ch==1:
		e=Employee.Employee()
		e.readEmployee()
		Emp_MongoDB.insertEmployee(e)

	elif ch==2:
		eno=int(input("Enter Empno to delete:"))
		Emp_MongoDB.deleteEmployee(eno)

	elif ch==3:
		eno=int(input("Enter EmpNo to Update:"))
		Emp_MongoDB.updateEmployee(eno)

	elif ch==4:
		eno=int(input("Enter Empno to search:"))
		Emp_MongoDB.searchEmployee(eno)

	elif ch==5:
		Emp_MongoDB.displayEmployees()

	elif ch==6:
		break
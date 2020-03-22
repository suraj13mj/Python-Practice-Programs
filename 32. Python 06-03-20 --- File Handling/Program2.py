#Program to create and store Employee Salary Records in a file

import os

def appendEmployee(eno,name,basic):
	fh=open("Employee.txt","a")
	hra=basic*0.10
	da=basic*0.73
	gross=basic+hra+da
	tax=gross*0.3
	net=gross-tax
	line=str(eno)+","+name+","+str(basic)+","+str(hra)+","+str(da)+","+str(gross)+","+str(tax)+","+str(net)+"\n"
	fh.write(line)
	fh.close()



def displayEmployees():
	fh=open("Employee.txt","r")
	for line in fh:
		emp=line.split(",")
		print("\nEmployee No:",emp[0],"\nEmployee Name:",emp[1],"\nBasic:",emp[2],"\nHRA:",emp[3],"\nDA:",emp[4],"\nGross Salary:",emp[5],"\nIncome Tax:",emp[6],"\nNet Salary:",emp[7])
	fh.close()



def searchEmployee(eno):
	fh=open("Employee.txt","r")
	flag=False
	for line in fh:
		emp=line.split(",")
		if(int(emp[0])==eno):
			print("\nEmployee No:",emp[0],"\nEmployee Name:",emp[1],"\nBasic:",emp[2],"\nHRA:",emp[3],"\nDA:",emp[4],"\nGross Salary:",emp[5],"\nIncome Tax:",emp[6],"\nNet Salary:",emp[7])
			flag=True
			break
	if flag==False:
		print("Employee record not found")
	fh.close()



def deleteEmployee(eno):
	count=0
	fh=open("Employee.txt","r")
	ftemp=open("Temp.txt","w")
	for line in fh:
		emp=line.split(",")
		if(int(emp[0])!=eno):
			ftemp.write(line)
		else:
			count+=1
			continue
	fh.close()
	ftemp.close()

	if count==0:
		print("Employee record not found")
		os.remove("Temp.txt")
	else:
		print("No of Employee records deleted:",count)
		os.remove("Employee.txt")
		os.rename("Temp.txt","Employee.txt")




def modifyEmployee(eno):
	count=0
	fh=open("Employee.txt","r")
	ftemp=open("Temp.txt","w")
	for line in fh:
		emp=line.split(",")
		if(int(emp[0])==eno):
			print("Existing Employee record:")
			print("\nEmployee No:",emp[0],"\nEmployee Name:",emp[1],"\nBasic:",emp[2],"\nHRA:",emp[3],"\nDA:",emp[4],"\nGross Salary:",emp[5],"\nIncome Tax:",emp[6],"\nNet Salary:",emp[7])
			print("Enter New Employee details")
			emp[1]=input("Enter Employee Name:")
			emp[2]=int(input("Enter Employee Basic Salary:"))
			emp[3]=emp[2]*0.10										#HRA
			emp[4]=emp[2]*0.73										#DA
			emp[5]=emp[2]+emp[3]+emp[4]								#Gross
			emp[6]=emp[5]*0.3										#Tax
			emp[7]=emp[5]-emp[6]
			print(emp[0])									#Net
			line=emp[0]+","+emp[1]+","+str(emp[2])+","+str(emp[3])+","+str(emp[4])+","+str(emp[5])+","+str(emp[6])+","+str(emp[7])+"\n"
			count+=1
		ftemp.write(line)

	fh.close()
	ftemp.close()

	if count==0:
		print("Employee record not found")
		os.remove("Temp.txt")
	else:
		print("No of Employee records modified:",count)
		os.remove("Employee.txt")
		os.rename("Temp.txt","Employee.txt")



if __name__=="__main__":
	while True:
		ch=int(input("1->New Employee  2->Display Employee records  3->Search Employee  4->Delete Employee  5->Modify Employee  6->Exit\n"))
		if ch==1:
			eno=int(input("Enter Employee No:"))
			name=input("Enter Employee Name:")
			basic=int(input("Enter Employee Basic salary:"))
			appendEmployee(eno,name,basic)

		elif ch==2:
			displayEmployees()

		elif ch==3:
			eno=int(input("Enter Employee No to search:"))
			searchEmployee(eno)

		elif ch==4:
			eno=int(input("Enter Employee No to delete:"))
			deleteEmployee(eno)

		elif ch==5:
			eno=int(input("Enter Employee No to modify:"))
			modifyEmployee(eno)

		else:
			break


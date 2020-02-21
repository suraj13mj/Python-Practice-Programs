#Program to store N Employee details, each Employee identified by Aadhaar No using Nested Dictionary


N=int(input("Enter the No of Employees:"))
emp={}
for i in range(0,N):
	uid=input("Enter Aadhaar Number:")
	temp={}
	temp["name"]=input("Enter Employee Name:")
	temp["eno"]=int(input("Enter Employee No:"))
	temp["basic"]=int(input("Enter Basic Salary:"))
	temp["hra"]=0.1*temp["basic"]
	temp["da"]=0.73*temp["basic"]
	temp["gross"]=temp["basic"]+temp["hra"]+temp["da"]
	temp["tax"]=0.3*temp["gross"]
	temp["net"]=temp["gross"]-temp["tax"]
	emp[uid]=temp

print("\nEmployee Details are:")
for uid in emp:
	print(emp[uid])
	print("\nAadhaar No:"+str(uid),"\nName:"+emp[uid]["name"],"\nEmployee No:"+str(emp[uid]["eno"]),"\nBasic Salary:"+str(emp[uid]["basic"]),"\nHRA:"+str(emp[uid]["hra"]),"\nDA:"+str(emp[uid]["da"]),"\nGross Salary:"+str(emp[uid]["gross"]),"\nIncome Tax"+str(emp[uid]["tax"]),"\nNet Salary:"+str(emp[uid]["net"]))
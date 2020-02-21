#Program to store Employee details in a Dictionary



emp={}

emp["name"]=input("Enter Employee Name:")
emp["eno"]=int(input("Enter Employee No:"))
emp["basic"]=int(input("Enter Basic Salary:"))
emp["hra"]=0.1*emp["basic"]
emp["da"]=0.73*emp["basic"]
emp["gross"]=emp["basic"]+emp["hra"]+emp["da"]
emp["tax"]=0.3*emp["gross"]
emp["net"]=emp["gross"]-emp["tax"]


print("\nEmployee Details are:")
print("\nName:"+emp["name"],"\nEmployee No:"+str(emp["eno"]),"\nBasic Salary:"+str(emp["basic"]),"\nHRA:"+str(emp["hra"]),"\nDA:"+str(emp["da"]),"\nGross Salary:"+str(emp["gross"]),"\nIncome Tax"+str(emp["tax"]),"\nNet Salary:"+str(emp["net"]))
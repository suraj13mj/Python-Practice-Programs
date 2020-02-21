#Program to read Student details into Dictionary and append it a List

college=[]
N=int(input("Enter No of Students:"))
for i in range(0,N):
	stud={}
	stud["roll"]=int(input("\nEnter Roll No:"))
	stud["name"]=input("Enter Name:")
	stud["per"]=float(input("Enter Percentage:"))
	college.append(stud)

for stud in college:
	print("\nRoll No:",stud["roll"],"\nName:",stud["name"],"\nPercentage:",stud["per"])
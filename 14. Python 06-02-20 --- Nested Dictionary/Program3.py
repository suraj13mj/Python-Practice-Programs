# Menu-driven Program to store Student details using Nested Dictionary

college={}
while True:
	ch=int(input("\n1.Add New Student\n2.Display all Students\n3.Search Student record\n4.Modify Student Record\n5.Delete Student Record\n6.Exit\n"))

	if ch==1:
		usn=input("Enter Student USN:")
		if usn in college:
			print("\nStudent Record already exists with this USN")
		else:
			s={}
			s["roll"]=int(input("Enter Roll No:"))
			s["name"]=input("Enter Name:")
			s["per"]=float(input("Enter Percentage:"))
			college[usn]=s

	elif ch==2:
		for usn in college:
			print("USN:",usn,"Name:",college[usn]["name"],"Roll No:",college[usn]["roll"],"Percentage:",college[usn]["per"])

	elif ch==3:
		usn=input("Enter Student USN to Search:")
		if usn in college:
			print("USN:",usn,"Name:",college[usn]["name"],"Roll No:",college[usn]["roll"],"Percentage:",college[usn]["per"])
		else:
			print("Student Record not found")

	elif ch==4:
		usn=input("Enter Student USN to Modify:")
		if usn in college:
			s=college[usn]
			print("Existing details in Student Record:")
			print("USN:",usn,"Name:",college[usn]["name"],"Roll No:",college[usn]["roll"],"Percentage:",college[usn]["per"])
			print("Enter New Student details:")
			s["roll"]=int(input("Enter Roll No:"))
			s["name"]=input("Enter Name:")
			s["per"]=float(input("Enter Percentage:"))
			college[usn]=s
		else:
			print("Invalid Student USN")

	elif ch==5:
		usn=input("Enter Student USN to Delete:")
		if usn in college:
			print("Deleted Student Record:")
			print("USN:",usn,"Name:",college[usn]["name"],"Roll No:",college[usn]["roll"],"Percentage:",college[usn]["per"])
			del college[usn]
		else:
			print("Invalid Student USN")

	else:
		break


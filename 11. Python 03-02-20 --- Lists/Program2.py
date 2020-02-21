#Program to append N Student details into the List : List within a List

college=[]
N=int(input("Enter No of Students:"))
for i in range(0,N):
	print("Enter Student RollNo, Name and Percentage:")
	stud=[int(input()),input(),float(input())]
	college.append(stud)

print("Student Records are:")
for stud in college:
	print("RollNo:",stud[0],"Name:",stud[1],"Percentage:",stud[2])


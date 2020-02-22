#Program to Sort Student Class Objects based on their instance attribute 'percentage'

class Student:
	def __init__(self,rollno=0,name=' ',per=0.0):
		self.rollno=rollno
		self.name=name
		self.per=per

	def readStudent(self):
		self.rollno=int(input("\nEnter Rollno:"))
		self.name=input("Enter Name:")
		self.per=float(input("Enter Percentage:"))

	def __lt__(self,s2):
		if self.per<s2.per:
			return True
		else:
			return False

	def __str__(self):
		return "\nRollNo:"+str(self.rollno)+"\nName:"+self.name+"\nPercentage:"+str(self.per)


def sortStudent(college):
	for i in range(1,N):
		for j in range(0,N-1):
			if college[j]<college[j+1]:
				temp=college[j]
				college[j]=college[j+1]
				college[j+1]=temp

if __name__=="__main__":
	stud=[]
	N=int(input("Enter the No of Students:"))
	for i in range(0,N):
		s=Student()
		s.readStudent()
		stud.append(s)

	sortStudent(stud)
	print("\nStudents sorted based on Percentage:")
	for s in stud:
		print(s)



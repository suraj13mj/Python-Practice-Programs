import Student

class Marks(Student):
	def __init__(self,rollno=0,name=" ",marks1=0,marks2=0):
		Student.__init__(self,rollno,name)
					#OR
		#super().__init__(rollno,name)
		self.__marks1=marks1
		self.__marks2=marks2
		self.__total=self.__marks1+self.__marks2f

	def readMarks(self):
		Student.readStudent(self)
		self.__marks1=int(input("Enter Marks1:"))
		self.__marks2=int(input("Enter Marks2:"))
		self.__total=self.__marks1+self.__marks2

	def displayMarks(self):
		Student.displayStudent(self)
		print("Marks1:"+str(self.__marks1),"Marks2:"+str(self.__marks2),"Total:"+str(self.__total),sep="\n")




if __name__=="__main__":
	print("Single Inheritance")
	stud=Marks()
	stud.readMarks()
	stud.displayMarks()
#Program to demonstrate Access Specifiers in Python and Getter and Setter Property
#To create Student Database to compute Total Marks

class Student:
	def __init__(self,rollno=0,name=" ",marks1=0,marks2=0):
		self.__rollno=rollno
		self.__name=name
		self.__marks1=marks1
		self.__marks2=marks2
		self.__total=self.__marks1+self.__marks2

	"""
	def setRollno(self,rollno):
		if rollno>0:
			self.__rollno=rollno
		else:
			print("Invalid Rollno")
	def getRollno(self):
		return self.__rollno

	Rollno=property(getRollno,setRollno)
	"""
				#OR
	
	@property
	def Rollno(self):
		return self.__rollno

	@Rollno.setter
	def Rollno(self,rollno):
		if rollno>0:
			self.__rollno=rollno
		else:
			print("Invalid Rollno")

	@property
	def Name(self):
		return self.__name

	@Name.setter
	def Name(self,name):
		self.__name=name

	@property
	def Marks1(self):
		return self.__marks1

	@Marks1.setter
	def Marks1(self,marks1):
		self.__marks1=marks1
		self.__total=self.__marks1+self.__marks2

	@property
	def Marks2(self):
		return self.__marks2

	@Marks2.setter
	def Marks2(self,marks2):
		self.__marks2=marks2
		self.__total=self.__marks1+self.__marks2

	@property
	def Total(self):
		return self.__total



if __name__=="__main__":
	s=Student()
	s.Rollno=1
	s.Name="Amit"
	s.Marks1=40
	s.Marks2=50
	print("Rollno:"+str(s.Rollno),"Name:"+s.Name,"Marks1:"+str(s.Marks1),"Marks2:"+str(s.Marks2),"Total:"+str(s.Total),sep='\n')





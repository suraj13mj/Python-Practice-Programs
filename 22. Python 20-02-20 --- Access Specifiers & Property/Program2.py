#Program to demonstrate Access Specifiers in Python and Getter and Setter Property
#To create Employee Database to compute the Employee salaries

class Employee(object):
	def __init__(self,eno=0,name=" ",basic=0):
		self.__empno=eno
		self.__name=name
		self.__basic=basic
		self.__calcSalary()

	def __calcSalary(self):
		self.__hra=self.__basic*0.10
		self.__da=self.__basic*0.73
		self.__gross=self.__basic+self.__hra+self.__da
		self.__tax=self.__gross*0.3
		self.__net=self.__gross-self.__tax

	@property
	def Empno(self):
		return self.__empno
	@Empno.setter
	def Empno(self,eno):
		self.__empno=eno

	@property
	def Name(self):
		return self.__name
	@Name.setter
	def Name(self,name):
		self.__name=name

	@property
	def Basic(self):
		return self.__basic
	@Basic.setter
	def Basic(self,basic):
		self.__basic=basic
		self.__calcSalary()

	@property
	def Hra(self):
		return self.__hra

	@property
	def Da(self):
		return self.__da

	@property
	def Gross(self):
		return self.__gross

	@property
	def Tax(self):
		return self.__tax

	@property
	def Net(self):
		return self.__net




if __name__=="__main__":
	N=int(input("Enter the No of Employees:"))
	emp=[]
	for i in range(0,N):
		e=Employee()
		e.Eno=int(input("\nEnter %d Employee No:"%(i+1)))
		e.Name=input("Enter Name:")
		e.Basic=int(input("Enter Basic Salary:"))
		emp.append(e)
	
	for x in emp:
		print("\nEmpNo:"+str(x.Eno),"Name:"+x.Name,"Basic Salary:"+str(x.Basic),"HRA:"+str(x.Hra),"DA:"+str(x.Da),"Gross Salary:"+str(x.Gross),"Tax:"+str(x.Tax),"Net Salary:"+str(x.Net),sep="\n")

	
	


	
	
	
	




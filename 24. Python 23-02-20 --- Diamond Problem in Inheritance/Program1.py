"""
Program to demonstrate to Hierarchial Inheritance in Python

					 Media
					   ^
		   ____________|______________
		  |							  |
		Books					   Pendrive


"""

class Media:
	def __init__(self,title=" ",price=0):
		self.title=title
		self.price=price

	def readMedia(self):
		self.title=input("Enter Title:")
		self.price=int(input("Enter Price:"))

	def display(self):
		print("\nTitle:"+self.title,"\nPrice:"+str(self.price))


""" ----------------------------------------------------------------- """                                                        

class Book(Media):
	def __init__(self,title=" ",price=0,npages=0):
		super().__init__(title,price)
		self.npages=npages

	def read(self):
		super().readMedia()
		self.npages=int(input("Enter No of Pages:"))

	def display(self):
		super().display()
		print("No of Pages:"+str(self.npages))

"""------------------------------------------------------------------"""


class Pendrive(Media):
	def __init__(self,title=" ",price=0,cap=0):
		super().__init__(title,price)
		self.cap=cap

	def read(self):
		super().readMedia()
		self.cap=int(input("Enter Capacity of Pendrive:"))

	def display(self):
		super().display()
		print("Pendrive Capacity:"+str(self.cap))




if __name__=="__main__":
	med=[]
	N=int(input("Enter No of Media Files:"))
	for i in range(0,N):
		#b=None
		ch=int(input("\n1.Book\n2.Pendrive\n"))
		if ch==1:
			b=Book()
		else:
			b=Pendrive()
		b.read()
		med.append(b)

	for x in med:
		x.display()

#Menu driven Program to maintain Product details where each Product is identified Product ID (implemented using Dictonaries)

class Product:
	def __init__(self,name='',price=0,qty=0):
		self.pname=name
		self.pprice=price
		self.pqty=qty

	def readProduct(self):
		self.pname=input("Enter Product Name:")
		self.pprice=int(input("Enter Product Price:"))
		self.pqty=int(input("Enter Product Quantity:"))

	def displayProduct(self,pid):
		print("\nProduct ID:"+str(pid),"Name:"+str(self.pname),"Price:"+str(self.pprice),"Quantity:"+str(self.pqty),sep='\n')


def Main():
	products={}
	while True:
		ch=int(input("\n1.Add New Product\n2.Display all Products\n3.Modify Product\n4.Delete Product\n5.Search Product\n6.Exit\n"))
		if ch==1:
			pid=int(input("Enter Product ID:"))
			if pid in products.keys():
				print("Product ID already exits")
			else:
				p=Product()
				p.readProduct()
				products[pid]=p
		elif ch==2:
			for pid in products:
				products[pid].displayProduct(pid)
		elif ch==3:
			pid=int(input("Enter Product ID to modify:"))
			if pid in products.keys():
				print("Existing Product details:")
				products[pid].displayProduct(pid)
				print("Enter New Product Details")
				products[pid].readProduct()
			else:
				print("Invalid Product ID")
		elif ch==4:
			pid=int(input("Enter Product ID to delete:"))
			if pid in products.keys():
				print("Deleted Product details:")
				products[pid].displayProduct(pid)
				del products[pid]
			else:
				print("Invalid Product ID")
		elif ch==5:
			pid=int(input("Enter Product ID to search:"))
			if pid in products.keys():
				print("Product details:")
				products[pid].displayProduct(pid)
			else:
				print("Invalid Product ID")
		else:
			break
Main()



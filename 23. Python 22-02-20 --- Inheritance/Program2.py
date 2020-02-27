"""
Program to demostrate Multi-level Inheritance in Python with classes Shape, Rectangle and Box
Shape <---- Rectange <---- Box

                     Shape
					   |
		               |
		            Rectangle
		               |
		               | 
                      Box
"""
					   
class Shape:
	def __init__(self,dim1=0,dim2=0):
		self.dim1=dim1
		self.dim2=dim2

	def read(self):
		self.dim1=int(input("Enter Dimension 1:"))
		self.dim2=int(input("Enter Dimension 2:"))

	def display(self):
		print("\nDimension 1:"+str(self.dim1),"\nDimension 2:"+str(self.dim2))


""" ----------------------------------------------------------------- """ 


class Rectangle(Shape):
	def __init__(self,dim1=0,dim2=0):
		super().__init__(dim1,dim2)
		self.area=self.dim1*self.dim2

	def areaofRect(self):
		self.area=self.dim1*self.dim2
		print("Area of Rectangle:",self.area,"sq units")
		

""" ----------------------------------------------------------------- """ 


class Box(Rectangle):
	def __init__(self,dim1=0,dim2=0,dim3=0):
		super().__init__(dim1,dim2)
		self.dim3=dim3
		self.vol=self.area*self.dim3

	def read(self):
		super().read()
		self.dim3=int(input("Enter Dimension 3:"))

	def display(self):
		super().display()
		print("Dimension 3:"+str(self.dim3))

	def volofBox(self):
		self.vol=self.area*self.dim3
		print("Volume of Box:",self.vol,"cubic units")



if __name__=="__main__":
	print("Multi-level Inheritance")
	b=Box()
	b.read()
	b.display()
	b.areaofRect()
	b.volofBox()
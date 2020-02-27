#Program to demonstrate Stack operations using Exceptions and check for StackOverflow and StackUnderflow Error

class InvalidStackSize(Exception):
	def __str__(self):
		return "Error: Invalid Stack Size"

class StackOverflow(Exception):
	def __str__(self):
		return "Error: Stack Overflow"

class StackUnderflow(Exception):
	def __str__(self):
		return "Error: Stack Underflow"


class Stack:
	def __init__(self,size=0):
		if size<=0:
			raise InvalidStackSize()
		self.size=size
		self.lst=[]

	def push(self,data):
		if len(self.lst)==self.size:
			raise StackOverflow()
		self.lst.append(data)

	def pop(self):
		if len(self.lst)==0:
			raise StackUnderflow()
		return self.lst.pop()

	def display(self):
		print("Stack elements are:")
		for i in range(-1,-len(self.lst)-1,-1):
			print(self.lst[i],end=" ")


if __name__=="__main__":
	try:
		stk=Stack(int(input("Enter the Stack Size:")))
	except InvalidStackSize as e:
		print(e)
		exit()
	while 1:
		ch=int(input("\n1.Push\n2.Pop\n3.Display\n4.Exit\n"))
		if ch==1:
			try:
				stk.push(int(input("Enter Data to Push:")))
			except ValueError as e:
				print(e)
			except StackOverflow as e:
				print(e)
		elif ch==2:
			try:
				data=stk.pop()
				print("Popped element is",data)
			except StackUnderflow as e:
				print(e)
		elif ch==3:
			stk.display()
		else:
			break
"""
Program to demonstrate the Error Stack message displayed by Python Virtual Machine when an Error is not handled inside the code.
Here the Program gets terminated at line 10 and displays ZeroDivisionError

"""


def sub2():
	print("Hello from Sub2")
	s=10/0
	print("Result:",s)
	print("Bye from Sub2")

def sub1():
	print("Hello from Sub1")
	sub2()
	print("Bye from Sub1")

if __name__=="__main__":
	print("Hello from Main")
	sub1()
	print("Bye from Main")
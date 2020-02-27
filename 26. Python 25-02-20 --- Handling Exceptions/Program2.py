#Program to demonstrate the use of Single try block and multiple except blocks

try:
	x=int(input("Enter first value:"))
	y=int(input("Enter second value:"))
	z=x/y
except ValueError:
	print("Invalid Input data")
	x=y=z=0
except ZeroDivisionError:
	print("Error: Divide by Zero")
	z=0

print("Result:",z)
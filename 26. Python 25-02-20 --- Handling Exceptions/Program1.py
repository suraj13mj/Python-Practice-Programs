#Program to demonstrate the use of try....except statements to catch Error objects


x=y=z=0

try:
	x=int(input("Enter first value:"))
except ValueError:
	print("Invalid first data")
	x=0

try:
	y=int(input("Enter second value:"))
except ValueError:
	print("Invalid second data")
	y=0

try:
	z=x/y
except ZeroDivisionError:
	print("Error: Divide by Zero Error")
	z=0

print("Result:",z)


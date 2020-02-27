#Program to demonstrate Exception handling and accept correct input untill user enters in correct input



class SecondValueZero(Exception):
	def __str__(self):
		return "Second value can't be zero for division"


while 1:
	try:
		x=int(input("Enter 1st value:"))
	except ValueError:
		print("Invalid first data")
		continue
	break

while 1:
	try:
		y=int(input("Enter 2nd value:"))
		if y==0:
			raise SecondValueZero()
	except ValueError:
		print("Invalid second data")
		continue
	except SecondValueZero as e:
		print(e)
		continue
	break

try:
	z=x/y
except:
	print("Divide by Zero Error")
	z=0

print("Result:",z)
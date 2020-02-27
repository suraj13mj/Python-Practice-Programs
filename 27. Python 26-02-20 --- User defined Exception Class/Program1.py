#Program to define User defined Error class derived from the BaseException class
#To check whether a number is Even or Odd using Exceptions

class EvenException(Exception):
	def __str__(self):
		return "Number is Even"

class OddException(Exception):
	def __str__(self):
		return "Number is Odd"


def checkNumber(N):
	if N%2==0:
		raise EvenException()
	else:
		raise OddException()


if __name__=="__main__":
	try:
		N=int(input("Enter a number:"))
		checkNumber(N)
	except ValueError as v:
		print(v)
	except EvenException as e:
		print(e)
	except OddException as o:
		print(o)
#To check whether a number is Positive or Negative or Zero using Exceptions

class PositiveException(Exception):
	def __str__(self):
		return "Number is Postive"

class NegativeException(Exception):
	def __str__(self):
		return "Number is Negative"

class ZeroException(Exception):
	def __str__(self):
		return "Number is Zero"


def checkNumber(N):
	if N==0:
		raise ZeroException()
	elif N>0:
		raise PositiveException()
	else:
		raise NegativeException()


if __name__=="__main__":
	try:
		N=int(input("Enter Number:"))
		checkNumber(N)
	except ValueError as e:
		print(e)
	except ZeroException as e:
		print(e)
	except PositiveException as e:
		print(e)
	except NegativeException as e:
		print(e)
		
""" 
Program to Print the pattern

* 1 ** 2 *** 3 **** 4 ***** 5
* 1 ** 2 *** 3 **** 4 ***** 5
* 1 ** 2 *** 3 **** 4 ***** 5

"""

for i in range(1,4):
	for j in range(1,6):
		print("*"*j,j,end=" ")
	print()
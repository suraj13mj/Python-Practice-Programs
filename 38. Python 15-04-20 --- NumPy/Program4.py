# Program to find the Sum of Principal and Secondary Diagonal elements

import numpy as np 

def readMatrix():
	print("Enter order of the matrix:")
	r = int(input())
	c = int(input())
	arr = np.zeros((r,c),dtype = np.int8)
	print("Enter Matrix of order "+str(r)+"x"+str(c))
	for i in range(r):
		for j in range(c):
			arr[i,j] = int(input())
	return arr

if __name__ == "__main__":
	a = readMatrix()

	#Principal Diagonal Sum
	psum = 0
	if a.shape[0] == a.shape[1]:
		for i in range(len(a)):
			psum += a[i,i]
		print("Principal Diagonal Sum:",psum)
	else:
		print("Invalid matrix order")

	#Secondary Diagonal Sum
	ssum = 0
	j = len(a[0])-1

	if a.shape[0] == a.shape[1]:
		for i in range(len(a)):
			ssum += a[i,j]
			j -= 1
		print("Secondary Diagonal Sum:",ssum)
	else:
		print("Invalid matrix order")
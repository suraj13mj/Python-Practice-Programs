# Program to find the Sum, Difference and Transpose of Matrices

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
	b = readMatrix()

	#Sum
	if a.shape[1] == b.shape[1]:
		sm = a + b
		print("Sum of two matrices is\n",sm)
	else:
		print("Two matrix can't be added : unequal column size")

	#Difference
	if a.shape[1] == b.shape[1]:
		diff = a - b
		print("Difference of two matrices is\n",diff)
	else:
		print("Two matrix can't be subtracted : unequal column size")

	#Transpose
	print("Transpose of matrix A:\n",a.T)
	print("Transpose of matrix B:\n",b.T)
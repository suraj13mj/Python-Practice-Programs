# Program to read a m x n matrix and find the sum of each row and each column

import numpy as np

print("Enter the order of the Matrix:")
r = int(input())
c = int(input())

arr = np.zeros((r,c),dtype=np.int8)
print("Enter matrix of order "+str(r)+"x"+str(c))

for i in range(r):
	for j in range(c):
		arr[i,j] = int(input())

for i in range(r):
	row = arr[i,...]
	print("Sum of Row "+str(i)+"="+str(sum(row)))

for i in range(c):
	col = arr[...,i]
	print("Sum of Column "+str(i)+"="+str(sum(col)))
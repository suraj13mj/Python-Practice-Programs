# Program to read a matrix of order m x n and display

import numpy as np

print("Enter order of the matrix:")
r = int(input())
c = int(input())


arr = np.zeros((r,c),dtype=np.int8)
print("Enter the matrix of order "+str(r)+"x"+str(c))

for i in range(r):
	for j in range(c):
		arr[i,j] = int(input())

print("\nEntered Matrix is:")

print(arr)
	#OR
for row in arr:
	for data in row:
		print(data,end=" ")
	print("\n")
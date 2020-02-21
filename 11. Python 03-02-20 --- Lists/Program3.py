#Program to read a matrix of order 3 * 4 and display

print("Enter the matrix elements of order 3*4")
mat=[]
for i in range(0,3):
	mat.append([])
	for j in range(0,4):
		mat[i].append(int(input()))
		
print("Matrix:")
for i in range(0,3):
	print(" ")
	for j in range(0,4):
		print(mat[i][j],end=" ")
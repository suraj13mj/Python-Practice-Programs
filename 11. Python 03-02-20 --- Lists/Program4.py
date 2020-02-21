#Program to read a matrix of order 3 * 4 and Find the Sum of each row

print("Enter the matrix elements of order 3*4")
mat=[]
sm=[]
for i in range(0,3):
	mat.append([])
	for j in range(0,4):
		mat[i].append(int(input()))
	sm.append(sum(mat[i]))

print(mat)
print("Sum of each row in matrix is:")
for i in range(0,3):
	print("SUM["+str(i)+"]:",sm[i])
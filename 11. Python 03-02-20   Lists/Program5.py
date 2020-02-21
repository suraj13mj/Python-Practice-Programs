#Program to accept a 3*4 matrix and find the sum of each column

mat=[]
print("Enter matrix elements of order 3*4")
for i in range(0,3):
	mat.append([])
	for j in range(0,4):
		mat[i].append(int(input()))

print(mat)
for j in range(0,4):
	sm=0
	for i in range(0,3):
		sm+=mat[i][j]
	print("SUM of column",j,"=",sm)

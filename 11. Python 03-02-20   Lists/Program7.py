#Program to find the Sum of Secondary Diagonal elements

mat=[]
print("Enter matrix elements of order 3*3")
for i in range(0,3):
	mat.append([])
	for j in range(0,3):
		mat[i].append(int(input()))

print(mat)
k=2
sm=0
for i in range(0,3):
	sm+=mat[i][j]
	j=j-1
print("SUM of Secondary Diagonal elements is",sm)

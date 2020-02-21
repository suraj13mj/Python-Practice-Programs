#Program to find sum of Principle Diagonal elements

mat=[]
print("Enter matrix elements of order 3*3")
for i in range(0,3):
	mat.append([])
	for j in range(0,3):
		mat[i].append(int(input()))

print(mat)
sm=0
for i in range(0,3):
	sm+=mat[i][i]
print("SUM of Principle Diagonal elements is",sm)

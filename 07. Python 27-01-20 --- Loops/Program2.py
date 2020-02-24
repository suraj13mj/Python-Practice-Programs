#Program to find the Sum of the series using loops

# 1^2/1! - 2^2/2! + 3^2/3! - 4^2/4! --------- N^2/N!

sg=1
N=int(input("Enter the value of N for the series:"))
fact=1
i=1
sum=0
while i<=N:
	sum=sum+((i*2)/fact)*sg
	i=i+1
	fact=fact*i
	sg=sg*(-1)

for i in range(1,N+1):
	if i%2==0:
		print(str(i)+"^2/"+str(i)+"!",end=" + ")
	else:
		print(str(i)+"^2/"+str(i)+"!",end=" - ")

print("\nSum of the series:",sum)
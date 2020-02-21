#Program to find Sum of series : 1/1 + 1/2 + 1/3 + ......+1/N

def seriesSum(N):
	i=1
	sm=0
	while i<=N:
		sm=sm+1/i
		i+=1
	return(sm)

N=int(input("Enter the value of N:"))
sm=seriesSum(N)
print("Sum of the series :")
for i in range(1,N+1):
    term="1/"+str(i)
    print(term,sep='+',end=" ")
print("\n",sm)

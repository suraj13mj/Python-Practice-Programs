#Program to find the sum of digits in a number using functions

def sum_digit(num):
	sum=0
	while(num!=0):
		rem=num%10
		sum+=rem
		num=num//10      #Floor Division   OR  num=int(num/10)
	return(sum)


N=int(input("Enter the Number:"))
sum=sum_digit(N)
print("The Sum of Digits in %d is %d"%(N,sum))
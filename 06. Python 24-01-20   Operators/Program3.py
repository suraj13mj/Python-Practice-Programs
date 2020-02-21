#Program to accept 3 numbers and find the First Largest and Second Largest

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

L1=a
L2=b
if b>L1:
	L2=L1
	L1=b
	if  c<b and c>a:
		L2=c
if c>L1:
	L2=L1
	L1=c
	if b<c and b>a:
		L2=b

print("\nFirst Largest is",L1,"\nSecond Largest is",L2)
#Program to find the Second Largest element in a List

def secondLarge(a):
	first=a[0]
	second=0
	for i in range(1,len(a)):
		if a[i]>first:
			second=first
			first=a[i]
		elif a[i]>second:
			second=a[i]
	return second

a=[]
N=int(input("Enter the No of elements to append to a List:"))
print("Enter",N,"integer elements")
for i in range(0,N):
	a.append(int(input()))
second=secondLarge(a)
print("Second Largest element in the list :",second)

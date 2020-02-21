#Program to accept N integer elements and find the sum, minimum and maximum using Lists

lst=[]
N=int(input("Enter the No of elements:"))
print("Enter",N,"integer elements:")
for i in range(0,N):
	lst.append(int(input()))

sm=sum(lst)
print("Sum:",sum(lst))
print("Smallest element:",min(lst))
print("Largest element:",max(lst))
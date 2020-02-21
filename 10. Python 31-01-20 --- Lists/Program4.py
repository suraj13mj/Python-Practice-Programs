#Program to accept N array elements and delete all the occurences of given data

lst=[]
N=int(input("Enter the No of elements:"))
print("Enter",N,"integer elements")
for i in range(0,N):
	lst.append(int(input()))

data=int(input("Enter the element to delete:"))
c=lst.count(data)
if c==0:
	print("Element not found")
else:
	for i in range(1,c+1):
		lst.remove(data)
print(lst)
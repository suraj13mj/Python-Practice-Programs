#Program to accept N array elements and delete the first occurence of given data

lst=[]
N=int(input("Enter the No of elements:"))
print("Enter",N,"integer elements")
for i in range(0,N):
	lst.append(int(input()))

data=int(input("Enter the element to delete:"))
if lst.count(data)==0:
	print("Element not found")
else:
	lst.remove(data)
	print(lst)
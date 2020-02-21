#Program to accept N integer elements into the List and Search for a given data, if found display the position 

lst=[]
N=int(input("Enter the No of elements:"))
print("Enter",N,"integer elements:")
for i in range(0,N):
	lst.append(int(input()))

flag=False	
key=int(input("Enter data to search:"))
for i in range(0,N):								
	if lst[i]==key:											# if key in lst :This won't help in finding the position
		flag=True
		break
if flag:
	print("Data found at position:",i+1)
else:
	print("Data not found")



	# OR
# Using List methods: lst.count() and lst.index()

if lst.count(key)==0:
	print("Data not found")
else:
	i=lst.index(key)
	print("Data found at position:",i+1)
#Program to demonstrate List method implementation


lst=[10,20,30,40,50,60,70,80,90]
print(lst)


print("\n1. lst.append()")
print("Enter the integer element to append:")
lst.append(int(input()))
print(lst)


print("\n2. lst.pop()")
x=lst.pop()
print("Popped element is",x)
print(lst)


print("\n3. lst.pop(index)")
print("Enter the index to pop an element:")
index=int(input())
x=lst.pop(index)
print("Popped element is",x)
print(lst)


print("\n4. lst.insert(index,data)")
print("Enter the index and date to insert:")
index=int(input())
data=int(input())
lst.insert(index,data)
print(lst)


print("\n5. lst.extend(lst1)")
lst1=[11,22,33]
print("lst1:",lst1)
lst.extend(lst1)
print(lst)


print("\n6. lst.remove(data)")
print("Enter the element to remove from list:")
data=int(input())
lst.remove(data)
print(lst)


print("\n7. lst.index(data,start_index,end_index)")
print("To search an element in list and return it's index")
data=int(input("Enter the element to search:"))
index=lst.index(data)
print("Index of element",data,"is",index)


print("\n8. lst.count(data)")
data=int(input("Enter the data to identify No of occurences:"))
x=lst.count(data)
print("No of occurences of",data,"is",x)


print("\n9. lst.reverse()")
print("Present List:",lst)
lst.reverse()
print("Reversed List:",lst)


print("\n10. lst.sort()")
print("Ascending Order")
lst.sort()
print(lst)


print("\n11. lst.sort(reverse=True)")
print("Descending Order")
lst.sort(reverse=True)
print(lst)
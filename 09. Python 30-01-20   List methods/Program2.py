#Program to find the first, second, third occurences of an element in the list using lst.index() method


lst=[10,20,30,40,20,50,60,70,20,40,90]
print(lst)
print("Occurences of element 20")

first=lst.index(20)
print("First occurence of element 20 is at index:",first)

second=lst.index(20,first+1)
print("Second occurence of element 20 is at index:",second)

third=lst.index(20,second+1)
print("Third occurence of element 20 is at index:",third)


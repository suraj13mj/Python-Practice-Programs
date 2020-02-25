#Program to demonstrate to Dictionary methods and functions


dict={1:"Violet",2:"Indigo",3:"Blue",4:"Green",5:"Yellow",6:"Orange",7:"Red"}
print(dict)


print("\nAdding an element into the Dictionary")
dict[8]="Pink"
print(dict)



print("\nPoping an element from Dictionary")
(key,value)=dict.popitem()
print("Popped key:",key)
print("Popped value:",value)



key=int(input("\nEnter the key to pop an element:"))
value=dict.pop(key)			
#OR del dict[key]
print("Popped value:",value)



print("\nModifying Dictionary value")
key=int(input("Enter the key of the value to be modified:"))
dict[key]=input("Enter the new value:")
print(dict)



print("\nLength of the Dictionary is",len(dict))




print("\nSearching in Dictionary")
key=int(input("Enter the key to be searched:"))
if key in dict:
	print(key,"is present in Dictionary, it's value is",dict[key])
else:
	print(key,"not found in Dictionary")

"""  OR
if key not in dict:
	print(key,"not found in Dictionary")
else:
	print(key,"is present in Dictionary, it's value is",dict[key])
"""	



print("\nDisplaying all keys in the Dictionary:",dict.keys())



print("\nDisplaying all the values in the Dictionary:",dict.values())



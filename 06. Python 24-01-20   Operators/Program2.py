#Program to find the Largest of 3 numbers

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

Large=a
if b>Large:
	Large=b
if c>Large:
	Large=c

print("Largest of 3 numbers",a,b,c,"is",Large)
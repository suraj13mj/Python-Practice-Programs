#Program to demonstrate String Access

s="MISSISSIPPI"

for c in s:
	print(c,end=" ")
print()

    #OR

for i in range(0,len(s)):
	print(s[i],end=" ")
print()


#To display in reverse order

for i in range(-1,-12,-1):			#for i in range(-1,-len(s)-1,-1):
	print(s[i],end=" ")


""" 
Program to Print the pattern

1 2 3 4 5
---------
1 2 3 4 5
---------
1 2 3 4 5
---------

"""

for i in range(1,7):
	for j in range(1,6):
		if i%2==1:
			print(j,end=" ")
		else:
			print("-",end=" ")
	print()
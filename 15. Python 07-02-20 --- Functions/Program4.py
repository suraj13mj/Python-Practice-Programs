#Demonstrate use of global keyword


a=10
def display():
	global a        						#refers to a=10 instead of creating local variable a
	print("In Display function:",a)         #value:10
	a=25


print("In Main function:",a)				#value:10
display()
print("In Main function:",a)				#value:25
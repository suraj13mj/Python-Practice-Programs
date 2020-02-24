#Program to sort a 2D List


lst=[[25,13],[18,2],[19,36],[17,3]]

def sortby(element):				#sorts based on column 2
	return(element[1])


print("Before Sorting:",lst)
lst.sort(key=sortby)				
print("After Sorting:",lst)
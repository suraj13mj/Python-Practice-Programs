#Program to sort a 2D List


lst=[[25,13],[18,2],[19,36],[17,3]]

def sortby(el):				#sorts based on column 2
	return(el[1])

lst.sort(key=sortby(lst))
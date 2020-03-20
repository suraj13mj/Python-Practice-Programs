#Program to display numbers from Main thread and user created thread


import threading

class Display(threading.Thread):
	def __init__(self):
		super().__init__()

	def run(self):
		print("\nStart of Display",end=" ")
		i=1
		while i<=10:
			print("\nDisplay:"+str(i),end=" ")
			i+=1
		print("\nEnd of Display",end=" ")

if __name__=="__main__":
	print("\nStart of Main",end=" ")

	t1=Display()
	t1.start()

	i=100
	while i>=10:
		print("\nMain:"+str(i),end=" ")
		i-=10
	print("\nEnd of Main",end=" ")

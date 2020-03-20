#Program to display Natural numbers from 1 to 10 with a delay of 1 second after displaying every number

import time, threading

class DisplayNum(threading.Thread):
	def __init__(self):
		super().__init__()

	def run(self):
		print("\nStart of DisplayNum",end=" ")
		i=1
		while i<=10:
			print("\n"+str(i),end="")
			time.sleep(1)
			i+=1
		print("\nEnd of DisplayNum",end=" ")

if __name__=="__main__":
	print("\nStart of Main",end=" ")

	t1=DisplayNum()
	t1.start()
	t1.join()

	print("\nEnd of Main",end=" ")

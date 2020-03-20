#Program to assign names to the thread by passing as argument to Thread constructor

import threading

class PThreads(threading.Thread):
	def __init__(self,name):
		super().__init__()
		self.tname=name

	def run(self):
		i=10
		while i>0:
			print(self.tname+" thread is running")
			i-=1

if __name__=="__main__":
	t1=PThreads("1st")
	t2=PThreads("2nd")
	t3=PThreads("3rd")
	t4=PThreads("4th")

	t1.start()
	t2.start()
	t3.start()
	t4.start()
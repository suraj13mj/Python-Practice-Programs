#Program to assign thread name using the methods  t.setName() and retrive thread names using t.getName()

import threading

class PThread(threading.Thread):
	def __init__(self):
		super().__init__()

	def run(self):
		i=10
		while i>0:
			print(self.getName()+" thread is running")
			i-=1


if __name__=="__main__":
	t1=PThread()
	t2=PThread()
	t3=PThread()
	t4=PThread()

	t1.setName("1st")
	t2.setName("2nd")
	t3.setName("3rd")
	t4.setName("4th")

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	
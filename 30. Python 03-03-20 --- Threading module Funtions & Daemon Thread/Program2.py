#Program to demonstrate the User threads and Daemon thread

import threading, time

def Task1():
	print("Start of Task1:",threading.currentThread().name)
	time.sleep(0.1)
	print("End of Task1:",threading.currentThread().name)

def Task2():
	print("Start of Task2:",threading.currentThread().name)
	time.sleep(0.1)
	print("End of Task2:",threading.currentThread().name)


if __name__=="__main__":

	t1=threading.Thread(target=Task1,name="User Thread")

	t2=threading.Thread(target=Task2,name="Daemon thread")
	t2.setDaemon(True)

	t1.start()
	t2.start()


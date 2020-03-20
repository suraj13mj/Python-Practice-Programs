#Program to demonstrate the use of ennumerate() and countActive() function
#Program to make all threads as Daemon threads except the current thread


import threading

def Digits():
	for i in range(0,10):
		print("Digit:"+str(i))

def Alphabets():
	for i in range(65,91):
		print("Alphabet:"+chr(i))

def OddNo():
	for i in range(1,51):
		if i%2==1:
			print("Odd:"+str(i))

def EvenNo():
	for i in range(1,51):
		if i%2==0:
			print("Even:"+str(i))


if __name__=="__main__":
	print("Start of Main")

	t1=threading.Thread(target=Digits,name="Digits")
	t2=threading.Thread(target=Alphabets,name="Alphabets")
	t3=threading.Thread(target=OddNo,name="Odd")
	t4=threading.Thread(target=EvenNo,name="Even")

	t1.start()
	#t2.start()
	#t3.start()
	#t4.start()

	count=threading.activeCount()
	print("Number of Active Threads:",count)

	main_t=threading.currentThread()

	for ethread in threading.enumerate():
		if ethread is main_t:												#current thread can't be made as Daemon thread
			continue
		ethread.setDaemon(True)
		print(ethread.getName()+" thread is made as Daemon thread")

	print("End of Main")

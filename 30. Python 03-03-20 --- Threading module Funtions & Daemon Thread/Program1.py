#Program to demonstrate the use of Threading module fuction currentThread()
#Program to check whether thread is_alive() using currentThread reference
#Two threads for displaying Uppercase and Lowercase Alphabets

import threading, time

def upperCase():
	cthread=threading.currentThread()
	cthread.setName("Uppercase")

	if cthread.is_alive():
		for c in range(65,91):
			time.sleep(0.001)
			print("\n"+chr(c),end=" ")

def lowerCase():
	cthread=threading.currentThread()
	cthread.setName("Lowercase")

	if cthread.is_alive():
		for c in range(97,123):
			time.sleep(0.001)
			print("\n"+chr(c),end=" ")

if __name__=="__main__":
	t1=threading.Thread(target=upperCase,args=())
	t2=threading.Thread(target=lowerCase,args=())

	cthread=threading.currentThread()
	cthread.setName("Main")
	print(cthread.getName())
	

	t1.start()
	t2.start()
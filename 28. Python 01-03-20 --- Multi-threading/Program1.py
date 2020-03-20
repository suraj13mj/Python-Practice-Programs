#Program to demostrate the two ways of creating threads in Python
#First thread displays Hello World and Second thread displays Welcome to Python


import threading

def HelloWorld():
	i=0
	while i<10:
		print("HelloWorld")
		i+=1

class WelcomeToPython(threading.Thread):
	def __init__(self):
		super().__init__()

	def run(self):
		i=0
		while i<10:
			print("Welcome to Python")
			i+=1



if __name__=="__main__":

	#First thread
	t1=threading.Thread(target=HelloWorld,args=())

	#Second thread
	t2=WelcomeToPython()

	t1.start()
	t2.start()


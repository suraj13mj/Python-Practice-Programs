#Program to demonstrate Thread Synchronisation in Python

import threading, time

lck=threading.Lock()

def Unsync_Booking(msg):
	print("[{",end=" ")
	time.sleep(0.05)
	print(msg,end=" ")
	time.sleep(0.05)
	print("}] -->",end=" ")


def Sync_Booking(msg):
	lck.acquire()
	print("[{",end=" ")
	time.sleep(0.05)
	print(msg,end=" ")
	time.sleep(0.05)
	print("}] -->",end=" ")
	lck.release()



class WithOutSync(threading.Thread):
	def __init__(self,msg):
		super().__init__()
		self.msg=msg

	def run(self):
		Unsync_Booking(self.msg)


class WithSync(threading.Thread):
	def __init__(self,msg):
		super().__init__()
		self.msg=msg

	def run(self):
		Sync_Booking(self.msg)


if __name__=="__main__":
	print("\nUnsynced Booking of Ticket Phases\n")

	w1=WithOutSync(" Checking Ticket Availability ")
	w2=WithOutSync(" Enter Passenger Details ")
	w3=WithOutSync(" Complete the Payment ")
	w4=WithOutSync(" Tickets Booked ")

	w1.start()
	w2.start()
	w3.start()
	w4.start()

	w1.join()
	w2.join()
	w3.join()
	w4.join()



	print("\n\nSynchronised Booking of Ticket Phases\n")

	s1=WithSync(" Checking Ticket Availability ")
	s2=WithSync(" Enter Passenger Details ")
	s3=WithSync(" Complete the Payment ")
	s4=WithSync(" Tickets Booked ")

	s1.start()
	s2.start()
	s3.start()
	s4.start()
	
	



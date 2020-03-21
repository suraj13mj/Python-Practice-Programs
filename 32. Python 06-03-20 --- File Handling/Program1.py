#Program to demonstrate basic file operations in Python

def createFile(filename):
	fh=open(filename,"w")
	print("Enter File contents:")
	print("Enter '#' to exit")
	while True:
		line=input()
		if line=="#":
			break
		fh.write(line+"\n")
	fh.close()



def appendData(filename):
		fh=open(filename,"a")
		print("Enter the data to append:")
		print("Enter # to exit")
		while True:
			line=input()
			if line=='#':
				break
			fh.write(line+"\n")
		fh.close()
	

	
def displayFile_1(filename):
	try:
		fh=open(filename,"r")
		print("\nFile contents are:\n")
		data=fh.read()
		print(data)
		fh.close()
	except Exception:
		print("File does not exist")

	#OR

def displayFile_2(filename):
	try:
		fh=open(filename,"r")
		print("\nFile contents are:\n")
		for line in fh:
			print(line,end="")
		fh.close()
	except Exception as e:
		print(e)



if __name__=="__main__":
	while True:
		ch=int(input("\n1.Create New File   2.Display File contents   3.Append Data to the File   4.Exit\n"))
		if ch==1:
			fnm=input("Enter the Filename to Create:")
			createFile(fnm)
		elif ch==2:
			fnm=input("Enter the Filename to Open:")
			displayFile_2(fnm)
		elif ch==3:
			fnm=input("Enter the Filename to append Data:")
			appendData(fnm)
		else:
			break



#Program to Print Hello World message in a Separate file : hello.txt


f1=open("C:\\Users\\Geralt\\Desktop\\Python\\I-O Statements\\hello.txt","w")            #Prints in Separate file
print("Hello World....!!!....Welcome to Python",file=f1)
f1.close()


import sys																				#Bydefault is printed in Standard Output
print("Hello World....!!!....Welcome to Python",file=sys.stdout)

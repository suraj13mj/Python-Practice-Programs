#Program to demonstrate the usage of functions to maintain Student Records 
#With functionalities to 1.Add New Student record 2.Display 3.Search 4.Delete 5.Modify

def newStudent(bvb):
	usn=input("Enter Student USN:")
	if usn in bvb.keys():
		print("USN already exists in Student records")
	else:
		bvb[usn]['roll']=int(input('Enter Student Roll No:'))
		bvb[usn]['name']=input('Enter Student Name:')
		bvb[usn]['per']=float(input('Enter Student Percentage:'))

def displayStudents(bvb):
	for key in bvb:
		print('USN:'+str(bvb[key]),'Roll No:'+str(bvb[key][roll]),'Name:'+str(bvb[key['roll']]),'Percentage:'+str(bvb[key]['per']),sep='\n')

def searchStudent(bvb,usn):
	if key in bvb.keys():
		print('USN:'+str(bvb[key]),'Roll No:'+str(bvb[key][roll]),'Name:'+str(bvb[key['roll']]),'Percentage:'+str(bvb[key]['per']),sep='\n')
	else:
		print('Student Record not found')

def deleteStudent(bvb,usn):
	if key in bvb.keys():
		print('Deleted Student Record:')
		print('USN:'+str(bvb[key]),'Roll No:'+str(bvb[key][roll]),'Name:'+str(bvb[key['roll']]),'Percentage:'+str(bvb[key]['per']),sep='\n')
		del bvb[key]
	else:
		print('Student Record not found')

def modifyStudent(bvb,usn):
	if key in bvb.keys():
		print('Existing Student record:')		
		print('USN:'+str(bvb[key]),'Roll No:'+str(bvb[key][roll]),'Name:'+str(bvb[key['roll']]),'Percentage:'+str(bvb[key]['per']),sep='\n')
		print('Enter New Student details:')
		bvb[usn]['roll']=int(input('Enter Student Roll No:'))
		bvb[usn]['name']=input('Enter Student Name:')
		bvb[usn]['per']=float(input('Enter Student Percentage:'))
	else:
		print('Student Record not found')


bvb={}
while True:
	ch=int(input('1.Add New Student\n 2.Display all Students\n  3.Search Student details\n  4.Delete Student Record\n  5.Modify Student Record\n  6.Exit\n'))
	if ch==1:
		newStudent(bvb)
	if ch==2:
		displayStudents(bvb)
	if ch==3:
		usn=input('Enter USN to Search:')
		searchStudent(bvb,usn)
	if ch==4:
		usn=input('Enter USN to Search:')
		deleteStudent(bvb,usn)
	if ch==5:
		usn=input('Enter USN to Search:')
		modifyStudent(bvb,usn)
	if ch==6:
		break


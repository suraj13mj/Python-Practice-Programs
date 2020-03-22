#Program to demonstrate the MySQL database connection using Python

import Student
import Student_DB

while True:
	ch=int(input("\n1->New Student  2->Delete Student  3->Update Student  4->Search Student  5->Display Students  6->Exit\n"))
	if ch==1:
		s=Student.Student()
		s.readStudent()
		Student_DB.insertStudent(s)

	elif ch==2:
		rno=int(input("Enter Rollno to delete:"))
		lst=Student_DB.searchStudent(rno)
		if not lst:
			print("Record not found")
		else:
			print("Deleted Student details:",lst[0])
			Student_DB.deleteStudent(rno)

	elif ch==3:
		s=Student.Student()
		s.rollno=int(input("Enter Rollno to update:"))
		lst=Student_DB.searchStudent(s.rollno)
		if not lst:
			print("Record not found")
		else:
			print("Existing Student data:",lst[0])
			s.name=input("Enter name to modify:")
			s.per=float(input("Enter percentage to modify:"))
			Student_DB.updateStudent(s)

	elif ch==4:
		rno=int(input("Enter Rollno to search:"))
		lst=Student_DB.searchStudent(rno)
		if not lst:
			print("Record not found")
		else:
			print("Student:",lst[0])

	elif ch==5:
		lst=Student_DB.fetchStudents()
		print(lst)
		for s in lst:
			print("\nRollno:",s[0],"\nName:",s[1],"\nPercentage:",s[2])

	elif ch==6:
		break
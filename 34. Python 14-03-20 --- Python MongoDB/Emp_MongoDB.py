import pymongo

try:
	client=pymongo.MongoClient("mongodb://localhost:27017")
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

db=client["employee_mdb"]
col=db["employee"]




def insertEmployee(e):
	emp={'empno':e.eno,'name':e.name,'salary':e.salary}
	result=col.insert(emp)
	print("Employee inserted with Id:",result)



def displayEmployees():
	docs=col.find({},{"_id":0,"empno":1,"name":1,"salary":1})
	for d in docs:
		print(d)



def deleteEmployee(eno):
	emp={'empno':eno}
	result=col.remove(emp)

	for x in col.find({},{"_id":0,"empno":1,"name":1,"salary":1}):
		print(x)


	

def updateEmployee(eno):
	name=input("Enter the New name to be updated:")
	salary=int(input("Enter the New salary to be updated:"))

	query={"empno":eno}
	new_val={"$set":{"name":name,"salary":salary}}
	col.update_one(query,new_val)

	for x in col.find({},{"_id":0,"empno":1,"name":1,"salary":1}):
		print(x)




def searchEmployee(eno):
	doc=col.find({'empno':eno},{"_id":0,"empno":1,"name":1,"salary":1})
	for x in doc:
		print(x)


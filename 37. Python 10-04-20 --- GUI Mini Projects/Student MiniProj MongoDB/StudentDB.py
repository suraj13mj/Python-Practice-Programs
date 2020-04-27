

#Connection to Backend MongoDB

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["tkinter_student"]
col = db["student"]


#Functions to perform CRUD operations in Backend MySQL

from Bean_Student import *

def insertStudent(stud):
    query = {'name':stud.Name,'roll':stud.Rollno,'address':stud.Address,'college':stud.College,'branch':stud.Branch,'sex':stud.Sex,'news':stud.News}
    result = col.insert_one(query)
    return True


"""
if __name__ == "__main__":
    stud = Student("Amit",1001,"Vidynagar,Hubli","BVB","CSE","MALE",1)
    insertStudent(stud)
"""


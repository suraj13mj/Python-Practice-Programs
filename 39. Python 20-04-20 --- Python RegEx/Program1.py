# Program to extract the Date, Time, SampleClass No, ErrorInfo, ID, and email ID from the sample.log file
# Using Python RegEx to extract Info from the Log file and write to separate file

import re

date_pattern = r"\d{4}-\d{2}-\d{2}"
time_pattern = r"\d{2}:\d{2}:\d{2}"
class_pattern = r"SampleClass\d"
error_pattern = r"\[[A-Z]+\]"
id_pattern = r"\d{9}"
email_pattern =r"\d{9} [A-Za-z].+@\w+.com"


#DATE
fh = open("sample.log","r")
fd = open("Datefile.txt","w")
for line in fh:
	date = re.findall(date_pattern,line)
	fd.write(str(date)+"\n")
fd.close()
fh.close()



#TIME
fh = open("sample.log","r")
ft = open("Timefile.txt","w")
times = re.findall(time_pattern,fh.read())
for time in times:
	ft.write(time+"\n")
ft.close()
fh.close()




#SampleClass No
fh = open("sample.log","r")
fs = open("SampleClass.txt","w")
sclasses = re.findall(class_pattern,fh.read())
for sclass in sclasses:
	fs.write(sclass+"\n")
fs.close()
fh.close()




#Error
fh = open("sample.log","r")
fe = open("Error.txt","w")
errors = re.findall(error_pattern,fh.read())
for error in errors:
	fe.write(error+"\n")
fe.close()
fh.close()





#IDs
fh = open("sample.log","r")
fi = open("IDs.txt","w")
ids = re.findall(id_pattern,fh.read())
for id in ids:
	fi.write(id+"\n")
fi.close()
fh.close()




#Emails
fh = open("sample.log","r")
fm = open("Emails.txt","w")
emails = re.findall(email_pattern,fh.read())
for email in emails:
	id,mail = email.split()
	fm.write(mail+"\n")
fs.close()
fh.close()
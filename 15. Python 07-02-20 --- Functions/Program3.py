#Demonstrate the use of Keyword Parameters

def Greet(name,id,phone,msg="Hello"):
	print(msg+" "+name)
	print(name+"'s ID is "+str(id))
	print(name+"'s Phone Number is "+str(phone)+"\n")



Greet("Anil",101,9885678498,"Good Afternoon")

Greet("Rajeev",102,msg="Have a Good day",phone=7896532145)    #Keyword Parameters

Greet("Gail",msg="Good Morning",phone=9632587425,id=103)

Greet(phone=9512398745,msg="Namaste",id=104,name='Subramanya')

#Greet("Sundar",phone=8523697415,msg='Hey',105)                #Error : Keyword Parameters must be always after Positional Parameters
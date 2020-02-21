#Program to find Simple Interest using Fuctions

def simpleInterest(p,t,r):
	s=(p*t*r)/100
	return(s)

P=int(input("Enter Principle amount:"))
T=int(input("Enter Time duration:"))
R=float(input("Enter Interest rate:"))
si=simpleInterest(P,T,R)
print("Simple Interest:",si)
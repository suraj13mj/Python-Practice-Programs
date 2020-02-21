#Program to demonstrate String Operations

s="KARNATAKA"
print(s)


print("\nlen() function")
length=len(s)
print("No of characters in",s,"is",length)



print("\nString Concatenation '+'")
s1="KARNATAKA"
s2="INDIA"

s3=s1+s2
   
s4=s+"INDIA"

s5="KARNATAKA"+" "+"INDIA"
print(s3,s4,s5,sep='\n')



print("\n'*' Operator for Strings")
s6="Hello"
s7=s6*20
s8="-----"*20
print(s6,s7,s8,sep='\n')




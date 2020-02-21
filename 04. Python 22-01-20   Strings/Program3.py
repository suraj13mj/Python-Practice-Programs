#Program to demonstrate String Slicing

s="SAVITASOFT HUBLI"
print(s)

s1=s[2:6]

s2=s[-8:-4]

s3=s[4:]

s4=s[:3]

s5=s[0:10:2]    #String with 1 character skip

s6=s[0:10:3]	#String with 2 character skips

s7=s[::4]

s8=s[::-1]		#String in reverse order

s9=s[::-2]		#String in reverse order with 1 skip

print(s1,s2,s3,s4,s5,s6,s7,s8,s9,sep="\n")
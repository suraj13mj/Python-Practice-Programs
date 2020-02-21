#Demonstrates that datatypes of class int String and Boolean cannot have duplicate objects

a=10
b=10
c=10

x="Hello"
y="Hello"
z="Hello"

m=True
n=True
o=True

p=3.65783
q=3.65783
r=3.65783

print('IDs of <class int> variables a b c:',id(a),id(b),id(c))

print('IDs of <class str> variables x y z:',id(x),id(y),id(z))

print('IDs of <class bool> variables m n o:',id(m),id(n),id(o))

print('IDs of <class float> variables p q r:',id(p),id(q),id(r))
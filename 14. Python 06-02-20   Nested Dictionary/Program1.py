#Program to Store Product details using Nested Dictionary

N=int(input("Enter the No of Products:"))
products={}
for i in range(0,N):
	pid=input("Enter Product ID:")
	p={}
	p["name"]=input("Enter Product Name:")
	p["price"]=int(input("Enter Product Price:"))
	p["stock"]=int(input("Enter Product Stock:"))
	products[pid]=p

print("\nProduct Details:")
for keys in products.keys():
	print(products[keys])              #displays in format: {name="Fan",price=1000,stock=23}
	print("\nPID:"+str(pid),"\nName:"+products[pid]["name"],"\nPrice:"+str(products[pid]["price"]),"\nStock:"+str(products[pid]['stock']))
#Demonstrate the use of Optional arguments

def carSpecs(model,brand='TATA',fuel='Petrol',pcapacity=4,cost=100000):
	print("Model Name:",model)
	print("Car Company:",brand)
	print("Fuel Type:",fuel)
	print("Passenger Capacity:",pcapacity)
	print("Price:",cost,end='\n\n')


carSpecs("SUV")				# brand, fuel, pcapacity, cost are Optional arguments

carSpecs("HatchBack","Hyundai")

carSpecs("Sports","Audi","Refined Diesel",2,34000000)

carSpecs()                  # Here 'model' is Not-an-Optional argument (Positional Argument) -> Error
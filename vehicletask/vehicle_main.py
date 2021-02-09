from car import Car
from truck import Truck 
from bicycle import Bicycle
from Vehicle_manager import VehicleManager

truck1 = Truck(1, 1000, 3)
truck2 = Truck(2, 3000, 2)
truck3 = Truck(3, 1000, 6)

car1 = Car(4, 5, 5)
car2 = Car(5, 7, 5)
car3 = Car(6, 4, 4)

bicycle1 = Bicycle(7, 4, "classic")
bicycle2 = Bicycle(8, 4, "road")
bicycle3 = Bicycle(9, 4, "folding")

vehicles = [truck1, truck2, truck3, car1, car2, car3, bicycle1, bicycle2, bicycle3]

vm = VehicleManager()
vm.vehicles = vehicles

available_trucks = vm.available_trucks()
print (f"Available Trucks: {available_trucks}")

vm.hire_vehicle (1, "31/01/2021")
print(f"Hiring out Truck 1:- {truck1}")
available_trucks = vm.available_trucks()
print (f"Available Trucks now: {available_trucks}")

print()

available_cars = vm.available_cars()
print (f"Available Cars:- {available_cars}")
vm.hire_vehicle(4, "01/02/2021")
vm.hire_vehicle(5, "01/02/2021")
print(f"Hiring out Car 1:- {car1}")
print(f"Hiring out Car 2:- {car2}")
available_cars = vm.available_cars()
print(f"Available Cars now: {available_cars}")
vm.return_vehicle(5, "03/02/2021")
print(f"Returning Car 2:- {car2}")
available_cars = vm.available_cars()
print(f"Available Cars now: {available_cars}")

print()


available_bicycles = vm.available_bicycles()
print(f"Available Bicycles: {available_bicycles}")
vm.hire_vehicle(9, "03/02/2021")
print(f"Hiring out Bicycle 3:- {bicycle3}")
available_bicycles = vm.available_bicycles()
print(f"Available Bicycles now: {available_bicycles}")
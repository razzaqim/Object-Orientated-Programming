from car import Car 

car1 = Car("Ford", 5, 70, 50)
print(car1)
print(car1.change_gear(4)) 

print(car1.speed_up(10))
print(car1.speed_up(25))

print(car1.slow_down(10))
print(car1.slow_down(60))
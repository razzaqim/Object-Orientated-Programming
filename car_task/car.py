class Car:
        """This is the Car class"""
        def __init__(self, manufacturer, current_gear, max_speed, current_speed):
            self.manufacturer = manufacturer
            self.current_gear = current_gear
            self.max_speed = max_speed
            self.current_speed = current_speed
    
        def change_gear(self, new_gear):
         return f"The car is now in gear {new_gear}"

        def speed_up(self, increment):
            if (self.current_speed + increment) > self.max_speed:
                return ("Sorry this is more than the max speed")
            else:
              return f"The speed of the car is now {self.current_speed + increment}"
    
        def slow_down(self, decrement):
              if (self.current_speed - decrement) < 0 :
                 return ("Sorry cannot slow down this much as it will reduce speed to below Zero")
              else:
                return f"The speed of the car is now {self.current_speed - decrement}"

        def __str__(self):
             return f"Manufacturer : {self.manufacturer}, current_gear: {self.current_gear}, max_speed: {self.max_speed}, current_speed:{self.current_speed}"
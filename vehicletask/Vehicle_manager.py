from car import Car
from truck import Truck 
from bicycle import Bicycle

class VehicleManager:
   vehicles = []
   def hire_vehicle(self, id, date):
      for vehicle in self.vehicles:
                if vehicle.id == id: 
                   vehicle.hire_date = date 
                   vehicle.return_date = "None"
                   return vehicle
        
   def return_vehicle(self, id, date):
      for vehicle in self.vehicles:
                if vehicle.id == id:
                    vehicle.hire_date = "None"
                    vehicle.return_date = date
                    return vehicle

   def available_trucks(self):
        trucks_list = []
        for vehicle in self.vehicles:
            if isinstance(vehicle, Truck) and vehicle.hire_date == "None" :
                trucks_list.append(vehicle.id)
        return trucks_list
   
   def available_cars(self):
          cars_list = []
          for vehicle in self.vehicles:
            if isinstance (vehicle, Car) and vehicle.hire_date == "None":
               cars_list.append(vehicle.id)
          return cars_list

   def available_bicycles(self):
         bicycles_list = []
         for vehicle in self.vehicles:
            if isinstance(vehicle, Bicycle) and vehicle.hire_date == "None":
                bicycles_list.append(vehicle.id)
         return bicycles_list 
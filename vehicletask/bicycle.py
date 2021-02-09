from PassengerVehicle import PassengerVehicle

class Bicycle(PassengerVehicle): 
    
    def __init__(self, id, max_num_of_passengers, classification):
        super().__init__(id, max_num_of_passengers)
        self.classification = classification
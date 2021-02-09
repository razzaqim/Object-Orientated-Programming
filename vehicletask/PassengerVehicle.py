from vehicle import Vehicle 

class PassengerVehicle(Vehicle):
    
    def __init__(self, id, max_num_of_passengers):
        super().__init__(id)
        self.max_num_of_passengers = max_num_of_passengers
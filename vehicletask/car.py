from PassengerVehicle import PassengerVehicle

class Car(PassengerVehicle):

    def __init__(self, id, max_num_of_passengers, num_of_doors):
        super().__init__(id, max_num_of_passengers)
        self.num_of_doors = num_of_doors

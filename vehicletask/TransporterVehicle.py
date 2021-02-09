from vehicle import Vehicle 

class TransporterVehicle(Vehicle):

    def __init__(self, id, load_capacity):
        super().__init__(id)
        self.load_capacity = load_capacity
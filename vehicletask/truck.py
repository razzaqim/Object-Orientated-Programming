from TransporterVehicle import TransporterVehicle

class Truck(TransporterVehicle):

    def __init__(self, id, load_capacity, num_of_axles):
        super().__init__ (id, load_capacity)
        self.num_of_axles = num_of_axles

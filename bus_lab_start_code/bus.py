class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []
    
    def drive(self):
        return "The wheels on the bus go blah blah blah!"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger_to_be_picked_up):
        self.passengers.append(passenger_to_be_picked_up)

    def drop_off(self, passenger_to_be_dropped_off):
        self.passengers.remove(passenger_to_be_dropped_off)

    def empty_bus(self):
        self.passengers.clear()
    
    def pick_up_from_stop(self, input_bus_stop):
        for individual in input_bus_stop.queue:
            self.passengers.append(individual)
        self.passenger_count()
        input_bus_stop.clear()



    

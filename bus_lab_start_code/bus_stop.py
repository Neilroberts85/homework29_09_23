class BusStop:
    def __init__(self, bus_stop_name):
        self.name = bus_stop_name
        self.queue = []

    def add_to_queue(self, input_person):
        self.queue.append(input_person)

    def clear(self):
        self.queue.clear()

    def queue_length(self):
        return len(self.queue)
    

 
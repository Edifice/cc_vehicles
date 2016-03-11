class Vehicle(object):

    count_list = []
    
    def __init__(self, registration_number):
        self.registration_number = registration_number
        Vehicle.count_list.append(self)
        Vehicle.count = len(Vehicle.count_list)
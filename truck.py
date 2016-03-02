from vehicle import Vehicle

class Truck(Vehicle):

	def __init__(self, registration_number, carrying_capacity):
		super(Truck, self).__init__(registration_number)
		self.carrying_capacity = carrying_capacity
		
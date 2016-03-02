from vehicle import Vehicle

class Motorcycle(Vehicle):

	def __init__(self, registration_number, acceleration):
		super(Motorcycle, self).__init__(registration_number)
		self.acceleration = acceleration

	def __str__(self):
		return 'motorcycle|{}|{}'.format(self.registration_number, self.acceleration)
		
from vehicle import Vehicle

class Car(Vehicle):

	def __init__(self, registration_number, number_of_seats):
		super(Car, self).__init__(registration_number)
		self.number_of_seats = number_of_seats
		

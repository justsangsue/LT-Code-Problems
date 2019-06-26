class VehicleType(Enum):



class Vehicle:
	def __init__(self, size, license):
		self.license = license
		self.size = size
		self.spots_taken = []

	def park(self, spot):
		if self.size <= spot.size:
			self.spots_taken.append(spot)

	def leave(self):
		self.spots_taken = []


class Motorcycle(Vehicle):
	def __init__(self, size, license):
		super(Motorcycle, self).__init__(0, license)


class Car(Vehicle):
	def __init__(self, size, license):
		super(Car, self).__init__(1, license)


class Bus(Vehicle):
	def __init__(self, size, license):
		super(Bus, self).__init__(2, license)	


class ParkingSpot:
	def __init__(self, size, taken):
		self.size = size
		self.taken = False

	def isAvailable(self):
		return self.taken

	def occupy(self, vehicle):
		vehicle.park(self)
		if len(vehicle.spots_taken) != 0:
			self.taken = True
		






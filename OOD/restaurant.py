class customer:
	def __init__(self, firstName, lastName, phoneNumber, email):
		self.firstName = firstName
		self.lastName = lastName
		self.phoneNumber = phoneNumber
		self.email = email

class restaurant:
	def __init__(self, restaurantName):
		self.restaurantName = restaurantName
		self.reservations = []

	def check_availablity(self, table, reservation):
		if table.size >= reservation.partySize and table.tableNumber > 0:
			return True

	def take_table(self, table, reservation):
		if self.check_availablity(table, reservation):
			table.tableNumber -= 1
			self.reservations.append()

	def leave_table(self, table):
		table.tableNumber += 1

class table:
	def __init(self, tableSize, tableNumber):
		self.tableSize = tableSize
		self.tableNumber = tableNumber

class reservation:
	def  __init__(self, restaurant, customer, partySize, timestamp):
		self.restaurant = restaurant
		self.customer = customer
		self.partySize = partySize
		self.timestamp = timestamp
		self.reservationID = None
		self.reservationInfo = {}

	def book(self):
        if self.restaurant.check_availablity(self, table):
        	reservationID = len(self.reservations) + 1
        	self.restaurant.take_table(self, table)
        	self.reservationID = reservationID
        	self.reservationInfo[self.reservationID] = self.restaurant

    def cancel(self):





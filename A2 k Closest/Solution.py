class Solution:
	"""
	@param numDestination, numDeliveries: integers
	@param allLocations: list of points (x, y)
	@return list of closest numDeliveries points
	"""
	def ClosestXdestinations(self, numDestinations, allLocations, numDeliveries):
		result = []
		if not allLocations or not allLocations[0] or numDeliveries > numDestinations:
			return result
		point_list = []
		for pt in allLocations:
			point = Point(pt)
			point_list.append(point)
		point_list.sort(key=lambda x : x.distance)

		for i in range(numDeliveries):
			result.append(point_list[i].coord)

		return result

class Point:
	def __init__(self, coord):
		self.coord = coord
		self.distance = coord[0] ** 2 + coord[1] ** 2

if __name__ == '__main__':
	numDestinations = 3
	allLocations = [[1, -2], [0, 0], [1, -23], [3, 5]]
	numDeliveries = 2

	sol = Solution()
	print(sol.ClosestXdestinations(numDestinations, allLocations, numDeliveries))
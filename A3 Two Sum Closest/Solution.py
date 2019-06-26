class Solution:
	"""
	@param maxTravelDist: integer
	@param forwardRouteList, returnRouteList: list of [index, distance]
	@return: list of pairs
	"""
	def findOptimalPairs(self, maxTravelDist, forwardRouteList, returnRouteList):
		if not forwardRouteList or not returnRouteList or not forwardRouteList[0] or not returnRouteList[0]:
			return []	
		forwardRouteList.sort(key=lambda x : x[1])
		returnRouteList.sort(key=lambda x : x[1])
		diff = maxTravelDist - (forwardRouteList[0][1] + returnRouteList[-1][1])
		result = [([0, 0], maxTravelDist)]
		i = 0
		j = len(returnRouteList) - 1
		while i < len(forwardRouteList) and j >= 0:
			if forwardRouteList[i][1] + returnRouteList[j][1] <= maxTravelDist:
				diff = maxTravelDist - (forwardRouteList[i][1] + returnRouteList[j][1])
				if diff <= result[0][1]:
					if diff < result[0][1]:
						result = []
					result.append(([forwardRouteList[i][0], returnRouteList[j][0]], diff))
					j -= 1
					continue
				else:
					i += 1
					continue
			else:
				j -= 1
				continue
			i += 1
		print(result)
		if result[0][0] == [0, 0]:
			return []
		return [ele[0] for ele in result]

if __name__ == '__main__':
	mtd = 10000
	fR = [[1, 1000], [4, 5000], [2, 7000], [3, 12000]]
	rR = [[1, 1000], [2, 3000], [5, 3000], [6, 5000], [3, 9000], [4, 20000]]

	sol = Solution()
	print(sol.findOptimalPairs(mtd, fR, rR))


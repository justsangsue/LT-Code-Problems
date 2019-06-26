from collections import deque

class Solution:
	"""
    @param numRow, numColumns: integers, size of grid
    @param lot: list, 2D matrix of grid
    @return: an integer
    """
	def removeObstacle(self, numRows, numColumns, lot):
		if not lot or not lot[0]:
			return -1

		step = self.bfs(lot, 0, 0)
		return step

	def bfs(self, grid, x, y):
		if grid[x][y] == 9:
			return 0
		q = deque([(x, y)])
		grid[x][y] = 0
		step = 0
		while q:
			l = len(q)
			for i in range(l):
				x, y = q.popleft()
				for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
					x_next = x + dx
					y_next = y + dy
					if not self.isValid(grid, x_next, y_next):
						continue
					q.append((x_next, y_next))
					if grid[x_next][y_next] == 9:
						return step + 1
					grid[x_next][y_next] = 0	
			step += 1
			#self.bprint(grid)
		return -1

	def isValid(self, grid, x, y):
		return 0 <= x < len(grid) and \
			   0 <= y < len(grid[0]) and \
			   (grid[x][y] == 1 or grid[x][y] == 9)

	def bprint(self, grid):
		for line in grid:
			print(line)
		print('\n')

def test(data):
	sol = Solution()
	print(sol.removeObstacle(len(data), len(data[0]), data))

if __name__ == '__main__':
	data1 = [[1, 0, 0],
	        [1, 0, 0],
	        [1, 9, 1]]
	data2 = [[]]
	data3 = [[1]]
	data4 = [[9]]
	data5 = [[1, 1]]
	data6 = [[1, 0, 0],
	         [1, 1, 0],
	         [0, 1, 9]]
	data7 = [[1, 1, 0],
			 [0, 1, 1],
			 [0, 0, 0],
			 [1, 9, 0]]
	data8 = [[1, 1, 1],
	  		 [1, 1, 1],
	  		 [1, 1, 1],
	  		 [1, 1, 1],
	  		 [1, 1, 9]]

	test(data1) # 3
	test(data2) # -1
	test(data3) # -1
	test(data4) # 0
	test(data5) # -1
	test(data6) # 4
	test(data7) # -1
	test(data8) # 6

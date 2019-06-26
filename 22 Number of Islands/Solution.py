from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        num_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    self.bfs(grid, x, y)
                    num_islands += 1
        return num_islands
    
    def bfs(self, grid, x, y):
        q = deque([(x, y)])
        grid[x][y] = False
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x_next = x + dx
                y_next = y + dy
                if not self.is_valid(grid, x_next, y_next):
                    continue
                q.append((x_next, y_next))
                grid[x_next][y_next] = False
    
    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]


if __name__ == '__main__':
    data = [[1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1]]
    data2 = [[1,1]]
    sol = Solution()
    print(sol.numIslands(data2))

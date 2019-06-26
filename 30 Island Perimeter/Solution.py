class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        peri = 0
        if not grid:
            return peri
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    peri += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        peri -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        peri -= 2
        return peri
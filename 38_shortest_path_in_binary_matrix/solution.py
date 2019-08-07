# Time complexity: O(MN)
# Space complexity: O(1)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (not grid) or (grid[0] == None) or (grid[0][0] == None) or (grid[0][0] == 1) or (grid[-1][-1] == 1):
            return -1
        
        x = len(grid)
        y = len(grid[0])
        
        from collections import deque
        q  = deque()
        q.append((0, 0))
        step = 0
        while q:
            l = len(q)
            step += 1
            for i in range(l):
                cur = q.popleft()
                for d in ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)):
                    cur_next = (cur[0] + d[0], cur[1] + d[1])
                    if 0 <= cur_next[0] and cur_next[0] < x and 0 <= cur_next[1] and cur_next[1] < y and grid[cur_next[0]][cur_next[1]] == 0:
                        if cur_next == (x - 1, y - 1):
                            return step + 1
                        q.append(cur_next)
                        grid[cur_next[0]][cur_next[1]] = 1
        return -1
            
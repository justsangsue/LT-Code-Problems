class Solution:
    def slidingPuzzle(self, board):
        if (not board) or (board[0] == None) or (board[0][0] == None):
            return -1
        if self.toNumber(board) == '123450':
            return 0
        visited = {}
        from collections import deque
        q = deque()
        q.append(self.toNumber(board))
        step = 0
        while q:
            l = len(q)
            print('-----', q, '-----')
            step += 1
            for i in range(l):
                cur = q.popleft()
                next_stages = self.getNext(cur)
                print(cur, next_stages)
                for next_cur in next_stages:
                    if next_cur not in visited:
                        if next_cur == '123450':
                            return step
                        visited.add(next_cur)
                        q.append(next_cur)
        return -1
    
    def toNumber(self, board):
        return ''.join([str(s) for s in board[0]]) + ''.join([str(s) for s in board[1]])
    
    def getNext(self, cur):
        pos = cur.find('0')
        res = []
        for d in (-3, 3, -1, 1):
            if (pos % 3 == 2 and d == 1) or (pos % 3 == 0 and d == -1):
                continue
            next_pos = pos + d
            
            if 0 <= next_pos and next_pos < 6:
                res.append(self.swapchr(cur, min(pos, next_pos), max(pos, next_pos)))
        return res
    
    def swapchr(self, s, pos1, pos2):
        return s[:pos1] + s[pos2] + s[pos1+1:pos2] + s[pos1] + s[pos2+1:]

if __name__ == '__main__':
    puzzle = [[0,1,2],[4,5,3]]
    sol = Solution()
    print(sol.slidingPuzzle(puzzle))
        
                    
                    
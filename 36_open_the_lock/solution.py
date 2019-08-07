class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if not target or target in deadends or '0000' in deadends:
            return -1
        deadends = set(deadends)
        from collections import deque
        q = deque()
        q.append('0000')
        step = 0
        while q:
            step += 1
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                for i in range(4):
                    cur_next = cur[:i] + str((int(cur[i:i+1]) + 1) % 10 ) + cur[i+1:]
                    if cur_next not in deadends:
                        if target == cur_next:
                            return step
                        deadends.add(cur_next)
                        q.append(cur_next)
                for i in range(4):
                    cur_next = cur[:i] + str((int(cur[i:i+1]) - 1 + 10) % 10 ) + cur[i+1:]
                    if cur_next not in deadends:
                        if target == cur_next:
                            return step
                        deadends.add(cur_next)
                        q.append(cur_next)
        return -1
                
                
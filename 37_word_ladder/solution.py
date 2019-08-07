# BFS
# 800 ms beat 8%
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or not beginWord or not endWord:
            return 0
        wordList = set(wordList)    
        visited = set()
        
        from collections import deque
        q = deque()
        q.append(beginWord)
        step = 0
        while q:
            l = len(q)
            step += 1
            for i in range(l):
                cur = q.popleft()
                for i in range(len(cur)):
                    for j in range(1, 26):
                        cur_next = cur[:i] + str(chr((ord(cur[i]) - 96 + j) % 26 + 96)) + cur[i+1:]
                        if cur_next not in visited and cur_next in wordList:
                            if cur_next == endWord:
                                return step + 1
                            visited.add(cur_next)
                            wordList.remove(cur_next)
                            q.append(cur_next)
        return 0

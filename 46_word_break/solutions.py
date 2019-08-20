class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if wordDict == None or len(wordDict) == 0:
            return False
        return self.dp({}, s, wordDict)
    
    def dp(self, mem, s, wordDict):
        if s in mem:
            return mem[s]
        
        if s in wordDict:
            mem[s] = True
            return True
        
        for i in range(1, len(s)):
            left = s[:i]
            if left in wordDict and self.dp(mem, s[i:], wordDict):
                mem[s] = True
                return True
        
        mem[s] = False
        return False
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S or S == '':
            return []
        h = dict()
        for i in range(len(S)):
            h[S[i]] = i
        result = []
        start = 0
        end = 0
        for i in range(len(S)):
            end = max(end, h[S[i]])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result

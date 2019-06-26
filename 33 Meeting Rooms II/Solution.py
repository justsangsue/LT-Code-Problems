"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals:
            return 0
        temp = []
        for interval in intervals:
            temp.append((interval.start, True))
            temp.append((interval.end, False))
        
        temp.sort(key=lambda x : (x[0], x[1]))
        
        result = 0
        maxNum = 0
        for t in temp:
            if t[1]:
                result += 1
            else:
                result -= 1
            maxNum = max(maxNum, result)
        return maxNum
            
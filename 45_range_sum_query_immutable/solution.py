class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = []
        s = 0
        for num in nums:
            s += num
            self.accu.append(s) 

    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j] if i == 0 else self.accu[j] - self.accu[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        for i in range(len(nums)):
            if i == 0:
                self.prefixSum.append(nums[i])
            else:
                self.prefixSum.append(nums[i] + self.prefixSum[-1])

    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
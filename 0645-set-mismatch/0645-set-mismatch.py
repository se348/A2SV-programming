class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = -1
        n= len(nums)
        
        for i in range(n):
            val = abs(nums[i])
            
            if nums[val - 1] <0:
                repeated = val
            else:
                nums[val -1] *= -1
        
        for i in range(1, n+ 1):
            if nums[i -1]>0:
                return [repeated, i]
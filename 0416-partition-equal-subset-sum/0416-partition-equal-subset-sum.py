class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        value = total / 2 
        
        memo = {}
        
        def dfs(ind, num):
            if num == 0:
                return True
            if ind >= len(nums):
                return False
            if (ind, num) in memo:
                return memo[(ind, num)]
            opt1 = dfs(ind + 1, num)
            if opt1:
                return True
            opt2 = dfs(ind + 1, num  - nums[ind])
            
            memo[(ind, num)] = opt1 or opt2
            
            return opt1 or opt2

        return dfs(0, value)
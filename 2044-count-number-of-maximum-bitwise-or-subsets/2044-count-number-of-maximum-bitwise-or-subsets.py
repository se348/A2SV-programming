class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        maxim = 0        
        def dfs(curr_index, curr_num):
            nonlocal maxim, count
            if curr_num == maxim:
                count += 1
            if curr_index == len(nums):
                return    
            
            for i in range(curr_index + 1, len(nums)):
                temp = curr_num | nums[i]
                dfs(i, temp)
        
        for num in nums:
            maxim = maxim | num
        dfs(-1, 0)
        return count
            
        
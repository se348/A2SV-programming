class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp ={}
        
        def dfs(start, end):
            if start == len(nums):
                return True
            if end >= n:
                return False
            if (start, end) in dp:
                return dp[(start, end)]
            
            if end == start + 1:
                if nums[start] != nums[end]:
                    return False
                
                cond1 = dfs(end + 1, end + 2)
                cond2 = dfs(end + 1, end + 3)
                dp[(start, end)] = cond1 or cond2
                
                return cond1 or cond2
            
            opt1 = nums[start] == nums[start + 1] == nums[start + 2]
            opt2 = nums[start + 1] - nums[start] == nums[start + 2] - nums[start + 1] == 1
            
            if opt1 or opt2:
                cond1 = dfs(end + 1, end + 2)
                cond2 = dfs(end + 1, end + 3)
                dp[(start, end)] = cond1 or cond2
                
                return cond1 or cond2
            
            dp[(start, end)] = False
            return False
        
        
        
        return dfs(0, 1) or dfs(0, 2)
            
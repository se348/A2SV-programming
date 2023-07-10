class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def dfs(ind, llist):
            if len(llist) >= 2:
                result.add(tuple(llist))
            
            for i in range(ind +1, len(nums)):
                if not llist or nums[i] >= llist[-1]:
                    llist.append(nums[i])
                    dfs(i, llist)
                    llist.pop()
                    
                    
        dfs(-1, [])
        return result
                
        
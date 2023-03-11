class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashed ={}
        running = 0
        res =0
        
        for ind, num in enumerate(nums):
            running += num
            
            if (2 * running - ind - 1) in hashed:
                res = max(res, ind - hashed[2 * running - ind - 1] + 1)
                
            hashed[2 *( running -num) - ind] = min(hashed.get(2 *( running -num) - ind, math.inf), ind)
            
        return res
            
        
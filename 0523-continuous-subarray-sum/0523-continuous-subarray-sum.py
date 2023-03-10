class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashed = {0: -1}
        prefix = 0
        
        for ind, num in enumerate(nums):
            prefix = (num + prefix) % k
            
            if prefix in hashed and (ind - hashed[prefix]) != 1:
                return True
            
            if prefix not in hashed:
                hashed[prefix] = ind
        
        return False
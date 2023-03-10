class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        hashed = {0: 0}
        
        res = math.inf
        running_sum = 0
        total = sum(nums) % p
        if total == 0:
            return 0
        for ind, num  in enumerate(nums):
            running_sum = (running_sum + num) % p
            
            if (running_sum - total) % p in hashed:
                res = min(res , ind- hashed[(running_sum - total) % p] + 1)
            hashed[running_sum] = ind + 1
        return res if res <len(nums) else -1
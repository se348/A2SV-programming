class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        runningsum = 0
        hashed =Counter()
        hashed[0] = 1
        
        ans =0
        for num in nums:
            runningsum += num
            ans += hashed[runningsum - goal]
            hashed[runningsum] += 1
        
        return ans
                
        
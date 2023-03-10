class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashed = defaultdict(int)
        hashed[0] = 1
        running_sum = 0
        
        count = 0
        
        for num in nums:
            running_sum = (running_sum + num) % k
            
            count += hashed[running_sum]
            
            hashed[running_sum] += 1
        
        return count
        
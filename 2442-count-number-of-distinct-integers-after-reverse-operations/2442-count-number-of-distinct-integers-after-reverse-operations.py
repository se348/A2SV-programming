class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        hashed = set(nums)
        
        for num in nums:
            
            hashed.add(int(str(num)[::-1]))
            
        return len(hashed)
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        length = len(nums)
        
        if length == 1:
            if nums[0] == 1:
                return True
            return False
        
        gcd_val = nums[0]
        
        for i in range(1, length):
            gcd_val = gcd(gcd_val, nums[i])
            
            if gcd_val == 1:
                return True
        
        return False        
        
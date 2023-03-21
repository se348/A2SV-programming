class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        left = 0
        res = 0
        
        while left < len(nums):
            if nums[left] != 0:
                left += 1
                continue
            
            right = left
            
            while right < len(nums) and nums[right] == 0:
                right += 1
            
            
            diff = (right -left)
            res += ((diff) * (diff + 1) //2)
            left = right
        
        return res
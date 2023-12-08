class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        even_parity = -1
        odd_parity = -1
        
        for i in range(len(nums) - 1, -1, -1):
            
            # check odd
            if nums[i] & 1:
                nums[i] = max(nums[i], nums[i] + even_parity - x, nums[i] + odd_parity)
                odd_parity = nums[i]
            else:
                nums[i] = max(nums[i], nums[i] + odd_parity - x, nums[i] + even_parity)
                even_parity = nums[i]
        
        return nums[0]
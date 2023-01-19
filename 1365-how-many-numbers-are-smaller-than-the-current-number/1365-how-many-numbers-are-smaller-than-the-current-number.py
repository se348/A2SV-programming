class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        for idx in range(len(nums)):
            nums[idx] = [nums[idx], idx]
            
        nums.sort()
        
        res= [ 0 ] * len(nums)
        
        prev_val = nums[0][0]
        past_idx = nums[0][1]
        
        for idx in range(1, len(nums)):
            val , prev_idx = nums[idx]
            if val != prev_val:
                res[prev_idx] = idx
                prev_val = val
                past_idx = prev_idx 
            else:
                res[prev_idx] = res[past_idx]
                
        return res
            
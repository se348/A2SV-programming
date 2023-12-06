class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        length = len(nums)
        
        if length <= 2:
            return True
        
        count = 0
        
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            count += 1
        
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                
                if i >= 2 and nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i - 2]
                    count += 1
                    
                else:
                    nums[i] = nums[i - 1]
                    count += 1
                    
            if count == 2:
                return False
        
        return True
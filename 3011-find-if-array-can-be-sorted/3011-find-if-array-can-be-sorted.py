class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        
        def count_setbits(curr_num):
            counts = 0
            
            while curr_num:
                if curr_num & 1:
                    counts += 1
                curr_num >>= 1
            
            return counts
            
        
        length = len(nums)
        
        
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                
                if nums[j - 1] > nums[j] and count_setbits(nums[j - 1]) == count_setbits(nums[j]):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                    
                else:
                    break
                
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                return False
        
        return True
                
        
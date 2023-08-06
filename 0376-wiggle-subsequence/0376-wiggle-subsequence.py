class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        INC, DEC = 1, -1
        n = len(nums)
        dp = {}
        
        for i in range(n -1, -1, -1):
            inc, dec = 0, 0 
            for j in range(i + 1, n):
                
                if nums[j] > nums[i]:
                    inc = max(inc, dp[(j, DEC)])
                    
                if nums[j] < nums[i]:
                    dec = max(dec, dp[(j, INC)])
            
            dp[(i, INC)] = inc + 1
            dp[(i, DEC)] = dec + 1
        
        return max(dp.values())
            
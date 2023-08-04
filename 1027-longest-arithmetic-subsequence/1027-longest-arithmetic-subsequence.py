class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # [20,1,15,3,10,5,8]
        n = len(nums)
        dp = {}
        temp = 0
        
        for i in range(n -2, -1, -1):
            for j in range( i+ 1, n):
                val = 1
                if (j, nums[i] - nums[j]) in dp:
                    val = dp[(j, nums[i] - nums[j])]
                    
                dp[(i, nums[i] - nums[j])] = max(val + 1, dp.get((i, nums[i] - nums[j]), 0))
                temp = max(temp, val + 1)
        return temp 
            
                
#         next_val, diff
#         (5, 3) : 1
#         (10, -5): 1
#         (10, -2): 1
#         (3, 7): 1
#         (3 , 2): 1
#         (3, 5): 1
#         (15, -12): 1
#         (15, -5): 2

        
            
        
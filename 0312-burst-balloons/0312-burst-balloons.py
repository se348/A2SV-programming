class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        
        @cache
        def dp(left,right):
            
            if left == right:
                return 0
            
            ans = 0
            l = 1 if left < 0 else nums[left]
            r = 1 if right >= len(nums) else nums[right]
            for i in range(left+1,right):
                
                val = l*nums[i]*r + dp(left,i) + dp(i,right)
                
                ans = max(ans,val)
            
            return ans%(10**9 + 7)
        
        return dp(-1,len(nums))
                
                       
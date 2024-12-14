class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        pref = [0] * (len(nums) + 1)
        
        for i in range(len(queries)):
            lf, rt = queries[i]
            
            pref[lf] += 1
            pref[rt + 1] -= 1
            
        
        for i in range(1, len(pref)):
            pref[i] = pref[i] + pref[i-1]
            
        
        for i in range(len(nums)):
            nums[i] = max(nums[i] - pref[i], 0)
            
        return sum(nums) == 0
        
        
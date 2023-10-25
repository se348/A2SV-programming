class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dfs(ind1, ind2):
            if ind1 == len(nums1) or ind2 == len(nums2):
                return 0
            
            
            count= -inf
            
            a = dfs(ind1 + 1, ind2 + 1)
            count = max(a + (nums1[ind1] * nums2[ind2] ), count)
                
            count = max(a, count)
            count = max(dfs(ind1 + 1, ind2), count)
            count = max(dfs(ind1, ind2 + 1), count)
            
            return count
        
        max_num1 =  max(nums1)
        max_num2 = max(nums2)
        
        min_nums1 =min(nums1)
        min_nums2 =min(nums2)
        
        if max_num1 < 0 and min_nums2 > 0:
            return max_num1 * min_nums2
        if max_num2 < 0 and min_nums1 > 0:
            return max_num2 * min_nums1
        
        return dfs(0, 0)
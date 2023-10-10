class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(ind, is_num_1):
            if ind == len(nums1) - 1:
                return 0
            
            smallest= inf
            if is_num_1:
                if nums1[ind + 1] > nums1[ind] and nums2[ind + 1] > nums2[ind]:
                    smallest = min(smallest,dp(ind + 1, True) ) 
                if nums2[ind + 1] > nums1[ind] and nums1[ind + 1] > nums2[ind]:
                    smallest = min(1 + dp(ind + 1, False), smallest)
            else:
                if nums1[ind + 1] > nums1[ind] and nums2[ind + 1] > nums2[ind]:
                    smallest = min(1 + dp(ind + 1, False), smallest)
                if nums2[ind + 1] > nums1[ind] and nums1[ind + 1] > nums2[ind]:
                    smallest = min(dp(ind + 1, True), smallest)
                
            return smallest
        
        return min(dp(0, True), 1 + dp(0, False))
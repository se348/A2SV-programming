class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(left_ptr, right_ptr):
            if left_ptr == len(nums1) or right_ptr == len(nums2):
                return 0
            
            if nums1[left_ptr] == nums2[right_ptr]:
                return dp(left_ptr + 1, right_ptr + 1) + 1
            
            option1 = dp(left_ptr + 1, right_ptr)
            option2 = dp(left_ptr, right_ptr + 1)

            return max(option1, option2)
        
        return dp(0, 0 )
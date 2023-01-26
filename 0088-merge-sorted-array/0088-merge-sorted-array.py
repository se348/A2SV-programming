class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        top = m - 1
        bottom = n - 1
        
        for started_pos in range(m +n -1, -1, -1):
            
            if bottom != -1 and (top ==  -1 or nums2[bottom] >= nums1[top]):
                nums1[started_pos] = nums2[bottom]
                bottom -=1
            
            else:
                nums1[started_pos] = nums1[top]
                top -= 1

        return nums1

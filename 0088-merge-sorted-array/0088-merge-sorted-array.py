class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
                
            left=n-1
            right=m-1
            flag = m+n -1
            while right >= 0 and  left >= 0:
                if  nums1[right] > nums2[left]:
                    nums1[flag] = nums1[right]
                    right-=1
                else:

                    nums1[flag] = nums2[left]
                    left-=1
                flag-=1
            while right>=0:
                nums1[flag] = nums1[right]
                right-=1
                flag-=1
            while left>=0:
                nums1[flag] = nums2[left]
                left-=1
                flag-=1

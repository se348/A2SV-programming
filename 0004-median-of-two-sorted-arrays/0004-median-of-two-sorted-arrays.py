class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        min_heap1, min_heap2 = [], []
        m, n = len(nums1), len(nums2)
        i, j =0 , 0
        
        
        def insert(number):
            
            if (i + j) < (((m + n) // 2)):
                heapq.heappush(min_heap1, -number)
            else:
                heapq.heappush(min_heap2, number)
        
        while i< m or j <n:
            if i!=m and (j == n or nums1[i] <= nums2[j]):
                insert(nums1[i])
                i += 1
            else:
                insert(nums2[j])
                j += 1
        if (n +m) & 1:
            return min_heap2[0]
        return (-min_heap1[0] + min_heap2[0]) / 2

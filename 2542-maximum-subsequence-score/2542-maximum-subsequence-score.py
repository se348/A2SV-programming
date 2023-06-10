class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_ver = [[nums2[i] ,nums1[i]] for i in range(len(nums1)) ]
        sorted_ver.sort(reverse = True)
        min_heap = []
        
        
        tot = 0
        res = 0
        
        for i in range(len(nums1)):
            if len(min_heap) < k:
                heapq.heappush(min_heap,sorted_ver[i][1])
                tot += sorted_ver[i][1]
                
                if len(min_heap) ==k:
                    res = max(res, tot * sorted_ver[i][0]) 
                    print(res)
            else:
                temp = heapq.heappop(min_heap)
                tot -= temp
                tot += sorted_ver[i][1]
                heapq.heappush(min_heap, sorted_ver[i][1])
                res = max(res, tot * sorted_ver[i][0]) 
        
        return res
                
        
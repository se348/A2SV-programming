from itertools import accumulate
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_num = 0
        
        for i, j in intervals:
            max_num = max(max_num, j)
            
        arr = [0] * (max_num + 1)
        
        for i, j in intervals:
            arr[i -1] += 1
            arr[j] -= 1
            
        return max(list(accumulate(arr)))
        
        
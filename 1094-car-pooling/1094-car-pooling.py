from itertools import accumulate
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_l = 0
        for i,j,k in trips:
            max_l =max(max_l, k)
        arr = [0] * (max_l + 1)
        
        for passeng, start, end in trips:
            arr[start] += passeng
            arr[end ] -= passeng
            
        curr = max(list(accumulate(arr)))
        if curr > capacity:
            return False
        return True
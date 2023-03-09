from itertools import accumulate
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1002
        
        for passeng, start, end in trips:
            arr[start] += passeng
            arr[end ] -= passeng
            
        curr = max(list(accumulate(arr)))
        if curr > capacity:
            return False
        return True
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 1
        
        for i in range(len(arr)):
            arr[i] = min(curr, arr[i])
            curr = arr[i] + 1
        
        return arr[-1]
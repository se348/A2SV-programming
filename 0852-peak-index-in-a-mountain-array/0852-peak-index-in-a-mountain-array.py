class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left = 0 
        right = len(arr) - 1
        res = 0
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if arr[mid] <= arr[mid + 1]:
                left = mid + 1
            
            else:
                res= mid
                right = mid - 1
                
        return res
                
            
            
            
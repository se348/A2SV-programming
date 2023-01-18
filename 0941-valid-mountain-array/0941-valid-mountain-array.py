class Solution:
    def findMaxIndex(self, arr):
        max_idx = -1
        max_val = -1
        for i in range(len(arr)):
            if arr[i] > max_val:
                max_idx = i
                max_val = arr[i]
        return max_idx
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        max_idx = self.findMaxIndex(arr)
        max_val = arr[max_idx]
        
        curr = -1
        
        if len(arr) < 3 or max_idx == 0 or max_idx == len(arr) - 1:
            return False
        
        
        for i in range(max_idx + 1):
            
            if arr[i] <= curr:
                return False

            curr = arr[i]

        curr = max_val
        
        for i in range(max_idx + 1, len(arr)):
            
            if arr[i] >= curr:
                return False
            
            curr = arr[i]
        
        return True
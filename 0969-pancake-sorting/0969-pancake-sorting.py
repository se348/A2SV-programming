class Solution:
    def findMax(self, arr, upToIndex):
        maxIdx = 0
        for i in range(1, upToIndex + 1):
            if arr[i]> arr[maxIdx]:
                maxIdx = i
        
        return maxIdx
    
    def swap(self,arr,idx):
        right = idx
        mid = (right) // 2
        
        for i in range(mid + 1):
            arr[i], arr[right] =arr[right], arr[i]
            right -= 1
            
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for idx in range(len(arr)-1,-1,-1):
            swap_idx = self.findMax(arr, idx)
            
            if swap_idx != idx:
                res.append(swap_idx+1)
                self.swap(arr, swap_idx)
                res.append(idx+1)
                self.swap(arr, idx)
        return res
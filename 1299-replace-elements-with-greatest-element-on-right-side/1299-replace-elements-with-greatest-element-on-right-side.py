class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
                
        curr_greatest = arr[-1]
        arr[-1] = -1
        
        for idx in range(len(arr)-2, -1, -1):
            tempo = curr_greatest
            
            if curr_greatest < arr[idx]:
                curr_greatest = arr[idx]
                
            arr[idx] = tempo
            
        return arr
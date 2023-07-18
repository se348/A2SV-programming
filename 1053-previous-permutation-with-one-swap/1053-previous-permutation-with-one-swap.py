class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        n= len(arr) -1
        if not n:
            return arr
        
        for i in range(n -1, -1,-1):
            if arr[i] <= arr[i + 1]:
                continue
            
            curr = n
            while i <= curr:
                
                if arr[i] > arr[curr]:
                    break
                curr -= 1
            
            while i!= curr and curr > 0 and arr[curr] == arr[curr - 1]:
                curr -= 1
            
            arr[i], arr[curr] =arr[curr], arr[i]
            break
        
        return arr
            
        
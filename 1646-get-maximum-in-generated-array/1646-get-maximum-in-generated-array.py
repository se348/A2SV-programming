class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr= [-1] * (n + 1)
        
        
        for i in range(n + 1):
            if i == 0:
                arr[i] = 0
            elif i == 1:
                arr[i] = 1
            
            elif not (i % 2 ):
                arr[i] = arr[i // 2]
            else:
                prev_elem_1 = arr[floor(i/ 2)]
                prev_elem_2 = arr[ceil(i/2)]
                
                arr[i] = prev_elem_1 + prev_elem_2
                
        return max(arr)
                
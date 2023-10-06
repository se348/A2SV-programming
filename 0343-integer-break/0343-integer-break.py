class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 2:
            return 1
        if n == 3:
            return 2
        
        arr = [1] *( n + 1)
        
        for i in range(2, n + 1):
            
            res = 0
            
            for j in range(1, i):
                
                diff = i - j
                temp1= diff * j
                temp2= arr[diff] * j
                temp3= diff * arr[j]
                temp4= arr[diff] * arr[j]
                
                res = max(temp1, temp2, temp3, temp4, res)
            
            arr[i] = res
            
        return arr[n]
    
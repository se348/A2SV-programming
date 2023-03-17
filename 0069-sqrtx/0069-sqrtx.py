class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        res= 0
        while left <= right:
            mid = (left + right) //2
            
            squared = mid**2
            
            if squared < x:
                res = mid
                left = mid +1
                
            elif squared > x:
                right = mid -1
                
            else:
                return mid
        return res
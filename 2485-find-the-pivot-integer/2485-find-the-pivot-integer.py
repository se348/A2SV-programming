class Solution:
    def pivotInteger(self, n: int) -> int:
        total = sum(range(n + 1))
         
        curr =0

        for i in range(n +1):
            prev= curr
            curr += i
            
            if curr == (total - prev):
                return i
            
            elif curr > (total - prev):
                return -1
        
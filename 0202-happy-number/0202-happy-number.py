class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n = str(n)
        
        while n!="1" and n not in seen:
            
            seen.add(n)
            tot =0
            for num in n:
                tot += (int(num) ** 2)
            n= str(tot)
        
        if n =="1":
            return True
        return False
class Solution:
    def evaluateSoln(self, piles, val):
        temp = 0
        for pile in piles:
            temp += math.ceil(pile/ val)
        return temp
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right = max(piles)
        
        res = 0
        
        while left <= right:
            mid =(left + right) //  2
            temp = self.evaluateSoln(piles, mid)
            
            if temp == h:
                res = mid
                right =mid -1
            
            elif temp > h:
                left =mid +1
            
            else:
                res= mid
                right =mid -1
                
        return res
            
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left= 0
        right = len(piles) - 1
        piles.sort()
        
        mine = 0
        while left < right:
            
            mine += piles[right - 1]
            
            left += 1
            right -=2
            
        return mine
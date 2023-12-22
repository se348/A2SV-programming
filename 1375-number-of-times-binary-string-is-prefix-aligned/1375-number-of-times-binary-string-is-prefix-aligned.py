class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        temp = [0]*len(flips)
        pref = 0
        post = 0
        ans = 0
        
        for indx, flip in enumerate(flips):
            
            if temp[indx]:
                pref += 1
                post -= 1
            
            temp[flip - 1] += 1
            if flip - 1 <= indx:
                pref += 1
            
            else:
                post += 1
            
            if pref == indx + 1 and not post:
                ans += 1
        
        return ans
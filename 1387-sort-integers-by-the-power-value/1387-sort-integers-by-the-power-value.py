class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        # 7 -> 11 -> 17 -> 13
         
        @cache
        def checkPowerValue(number):
            if number == 1:
                return 0
            elif number & 1:
                return 1 + checkPowerValue((number * 3) + 1)
            return 1 + checkPowerValue(number // 2)
            
        sorted_pows = []
        
        for i in range(lo, hi + 1):
            sorted_pows.append((checkPowerValue(i), i))
            
        sorted_pows.sort()
        return sorted_pows[k - 1][1]
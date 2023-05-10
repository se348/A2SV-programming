class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        mask =1
        for i in range(32):
            count = 0
            for num in nums:
                if num & mask:
                    count += 1
            if count % 3:
                res += mask
            mask *= 2
            
        if res >= 2 ** 31:
            res = -1 * (2 ** 32 - res)
        return res
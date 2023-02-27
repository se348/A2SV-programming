class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        remainder =[0] * k
        remainder[0] = 1
        
        curr = 0
        res = 0
        
        for num in nums:
            curr += num
            curr %= k
            if curr <0:
                curr +=k
            res += remainder[curr]
            remainder[curr] += 1
        
        return res
        
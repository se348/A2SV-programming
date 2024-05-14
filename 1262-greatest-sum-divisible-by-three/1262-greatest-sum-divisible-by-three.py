class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        result = sum(nums)
        
        nums.sort()
        
        ones = []
        twos = []
        
        for num in nums:
            if num % 3 == 1 and len(ones) < 2:
                ones.append(num)
            if num % 3 == 2 and len(twos) < 2:
                twos.append(num)
        if not result % 3:
            return result
        
        if result % 3 == 1:
            minim = inf
            if len(twos) >= 2:
                minim = twos[0] + twos[1]
            if len(ones) >= 1:
                minim = min(minim, ones[0])
            
            if minim == inf:
                return 0
            return result - minim
        
        minim = inf

        if len(ones) >= 2:
            minim = ones[0] + ones[1]
        if len(twos) >= 1:
            minim = min(minim, twos[0])

        if minim == inf:
            return 0
        return result - minim
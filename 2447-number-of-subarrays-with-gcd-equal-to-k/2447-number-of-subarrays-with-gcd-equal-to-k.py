class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        result = 0
        
        for i in range(len(nums)):
            if (nums[i] % k):
                continue
            
            paths= [nums[i]]
            if nums[i] == k:
                result += 1
            
            for j in range(i+ 1, len(nums)):
                if (nums[j] % k):
                    break
                paths.append(nums[j])
                currGcd = reduce(gcd, paths)
                
                if currGcd == k:
                    result += 1
        
        return result
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        length= len(nums)
        
        @cache
        def dp(count , bit_information):
            
            options = 0 
            
            for i in range(length):
                if( bit_information >> i) & 1:
                    continue
                for j in range(i+ 1, length):
                    if (bit_information >> j) & 1:
                        continue
                        
                    newNumber = bit_information | (1 << i) | (1 << j)
                    curr = dp(count + 1, newNumber)
                    options = max(options, curr + (count * math.gcd(nums[i], nums[j])))
            
            return options
        
        return dp(1, 0)
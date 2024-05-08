class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans= []

        current_xor = 0
        target = pow(2, maximumBit) -1
        
        for i in range(len(nums)):
            
            current_xor ^= nums[i]
            ans.append(current_xor ^ target)
            
            
        return reversed(ans)
            
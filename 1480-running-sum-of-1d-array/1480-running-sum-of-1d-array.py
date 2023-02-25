class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = []
        
        for i in range(len(nums)):
            
            if i == 0:
                prefixSum.append(nums[0])
            
            else:
                prefixSum.append(nums[i] + prefixSum[-1])
                
        return prefixSum
            
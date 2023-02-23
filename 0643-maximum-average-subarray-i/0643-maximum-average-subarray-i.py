class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        temp = max_sum
        
        for i in range(len(nums)-k):
            temp -= nums[i]
            temp += nums[i + k]
            max_sum = max(max_sum, temp)
        
        return max_sum / k
        
        
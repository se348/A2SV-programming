class Solution:
    def binary_search(self, targ, nums):
        left = 0    
        length = len(nums)
        right = length -1
        
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == targ:
                return mid
            
            elif nums[mid] < targ:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = list(set(nums))
        
        
        added = length - len(nums)
        
        nums.sort()
        res = inf
        
        
        for i in range(len(nums)):
            
            targ = nums[i] + length - 1
            ind = self.binary_search(targ, nums)

            res = min(res, length - ind - 1 + i)
        
        return max(res, added)
           
        
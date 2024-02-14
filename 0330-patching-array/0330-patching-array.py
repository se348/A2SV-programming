class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        patches = 0
        running_sum = 0
        
        if n > nums[-1]:
            nums.append(n)
        
        for i in range(len(nums)):
            
            while nums[i] > running_sum + 1 and running_sum < n:
              
                running_sum =  2 * running_sum + 1
                patches += 1
            
            running_sum += nums[i]
            
        return patches
            
        
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        numsset = set()
        rightptr =0
        
        for leftptr in range(len(nums)):
        
            while rightptr < len(nums) and nums[rightptr] in numsset:
                
                rightptr += 1
            
            if rightptr < len(nums):
                numsset.add(nums[rightptr])
                nums[leftptr] = nums[rightptr]
                
            if rightptr == len(nums):
                return leftptr

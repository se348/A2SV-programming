class Solution:
    def gt(self, left, right):
        return left + right > right + left
    
    def selection_sort(self, nums):
        for left in range(len(nums)):
            larger = left
            for right in range(left+1, len(nums)):
                if self.gt(nums[right], nums[larger]):
                    larger = right
            nums[left], nums[larger] = nums[larger], nums[left]
            
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            
        self.selection_sort(nums)
        
        return str(int("".join(nums)))
class Solution:
    def swap(self, nums, start, end):
        
        mid = (start + end) //2
        for ind in range(start, mid+1):
            nums[ind], nums[end] = nums[end], nums[ind]
            end -= 1
        
        
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        end = len(nums) -k -1
        self.swap(nums, 0, end)
        start = len(nums) - k
        end = len(nums) - 1
        self.swap(nums, start, end)
        self.swap(nums, 0, end)
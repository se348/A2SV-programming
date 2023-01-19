class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for idx in range(len(nums)):
            minim = idx
            for idx2 in range(idx,len(nums)):
                if nums[idx2] < nums[minim]:
                    minim = idx2
            
            nums[idx], nums[minim] = nums[minim], nums[idx]
            
        
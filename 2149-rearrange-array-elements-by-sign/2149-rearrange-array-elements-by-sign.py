class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = []
        negative_nums = []
        
        for num in nums:
            
            if num > 0:
                positive_nums.append(num)
            
            elif num < 0:
                negative_nums.append(num)
        
        ordered = []
        
        for i in range(len(positive_nums)):
            
            ordered.append(positive_nums[i])
            ordered.append(negative_nums[i])
            
        return ordered
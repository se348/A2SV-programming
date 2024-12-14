class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        window_elements = {}
        count = 0
        left_index = 0
        
        for i in range(len(nums)):
            
            for elem in list(window_elements.keys()):
                if abs(elem - nums[i]) > 2:
                    left_index = window_elements[elem] + 1
                    del window_elements[elem]
            
            window_elements[nums[i]] = i
            size = (i - left_index + 1)
            count += size
            
        return count
    
#         [1, 0, 2, 1, 0, 3, 3, 3, 2, 2]
# [4, 1, 0, 0, 3, 0, 3, 0, 0, 1]
# [4, 3, 4, 1, 4, 4, 2, 3, 3, 4]
# [1, 1, 2, 3, 1, 0, 0, 0, 2, 0]
# [4, 4, 3, 0, 3, 3, 2, 0, 0, 1]
# [4, 3, 1, 0, 1, 2, 2, 2, 3, 0]
# [4, 1, 4, 0, 4, 2, 3, 3, 0, 2]
# [4, 0, 1, 4, 3, 3, 0, 3, 3, 3]
# [2, 1, 2, 2, 2, 1, 1, 2, 2, 2]
# [4, 3, 4, 1, 1, 3, 0, 4, 2, 1]
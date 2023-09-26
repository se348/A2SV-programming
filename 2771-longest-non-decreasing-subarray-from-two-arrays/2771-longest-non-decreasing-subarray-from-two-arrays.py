class Solution:
    def maxNonDecreasingLength(self, nums_1: List[int], nums_2: List[int]) -> int:
        length = len(nums_1)
        
        memo_1 = [1] * length
        memo_2 = [1] * length
        
        for i in range(length - 2, -1, -1):
            curr_1 =nums_1[i]
            curr_2 =nums_2[i]
            
            if curr_1 <= nums_1[i + 1]:
                memo_1[i] = memo_1[i + 1] + 1
            if curr_1 <= nums_2[i + 1]:
                memo_1[i] = max(memo_1[i], memo_2[i + 1] + 1)
            
            if curr_2 <= nums_1[i + 1]:
                memo_2[i] = memo_1[i + 1] + 1
            if curr_2 <= nums_2[i + 1]:
                memo_2[i] = max(memo_2[i], memo_2[i + 1] + 1)
                
        return max(max(memo_1), max(memo_2))
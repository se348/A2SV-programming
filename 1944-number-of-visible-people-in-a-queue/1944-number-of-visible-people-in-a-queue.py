class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        monotonic_stack = []
        res = []
        
        for i in range(len(heights) - 1, -1, -1):
            
            
            count = 0
            while monotonic_stack and heights[i] > monotonic_stack[-1]:
                monotonic_stack.pop()
                count += 1
            
            res.append(count + (1 if monotonic_stack else 0))
            monotonic_stack.append(heights[i])
            
        return reversed(res)
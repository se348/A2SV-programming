class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = heights.copy()
        
        mono_stack = []
        
        for i in range(len(heights)):
            
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            
            if mono_stack:
                ans[i] += (i - mono_stack[-1] - 1) * (heights[i])
            else:
                ans[i] += (i ) * (heights[i])
            
            mono_stack.append(i)
            
        mono_stack = []
        
        for i in range(len(heights) -1, -1, -1):
            # print(mono_stack)            
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            
            if mono_stack:
                ans[i] += (mono_stack[-1] - i - 1) * (heights[i])
            else:
                ans[i] += ((len(heights) -1) - i ) * (heights[i])
            
            mono_stack.append(i)
        
        return max(ans)
                
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        
        intervals.sort()
        
        for i in range(len(intervals)):
            if stack and intervals[i][0] <= stack[-1][1]:
                stack[-1][1]  = max(stack[-1][1], intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack
        
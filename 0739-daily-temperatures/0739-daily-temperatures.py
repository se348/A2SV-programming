class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_ind = stack.pop()
                res[prev_ind] = (ind - prev_ind)
            stack.append((temp, ind))
        
        return res
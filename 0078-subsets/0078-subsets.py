class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def appender(path):
            tempo = []
            for i,j in path:
                tempo.append(i)
            result.append(tempo)
        def backtrack(path):
            appender(path)
            if len(path) == len(nums):
                return
            
            minimum = -1
            if path:
                minimum = path[-1][1]
            
            for i in range(minimum +1, len(nums)):
                path.append((nums[i], i))
                backtrack(path)
                path.pop()
        backtrack([])
        return result
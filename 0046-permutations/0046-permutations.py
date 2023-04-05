class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(num, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for elem in nums:
                if elem not in path:
            
                    path.append(elem)
                    dfs(elem, path)
                    path.pop()
            
        
        dfs(None, [])
        return ans
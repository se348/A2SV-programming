class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        smallerThanTarget = []
        
        for num in candidates:
            if num > target:
                break
            smallerThanTarget.append(num)
        
        res= set()
        traversed = set()
        def dfs(nums,i, total):
            curr = tuple(nums)
            
            if curr in traversed:
                return
            traversed.add(curr)
            
            if total == target:
                res.add(tuple(nums))
                return
            
            for j in range(i + 1, len(smallerThanTarget)):
                if total + smallerThanTarget[j] <= target:
                    nums.append(smallerThanTarget[j])
                    dfs(nums, j, total + smallerThanTarget[j])
                    nums.pop()
                    
        dfs([], -1, 0)
        return res
                
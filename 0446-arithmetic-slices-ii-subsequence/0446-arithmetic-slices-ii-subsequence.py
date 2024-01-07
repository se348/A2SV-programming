class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        diction = defaultdict(int)
        n = len(nums)
        res = 0
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                
                added = (diction[(j, nums[j] - nums[i])] +  1)
                res += max(added -1, 0)
                diction[(i, nums[j] - nums[i])] += added
                    
        count = Counter(nums)
        return res
                    
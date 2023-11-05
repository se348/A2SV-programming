class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = (n * (n - 1)) // 2
        hash_map = defaultdict(int)
        
        for i in range(n):
            
            count = hash_map[(nums[i] - i)]
            res -= count
            hash_map[(nums[i] - i)] += 1
        
        return res
            
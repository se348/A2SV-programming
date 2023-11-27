class Solution:

    def __init__(self, nums: List[int]):
        
        self.diction = defaultdict(list)
        
        for i in range(len(nums)):
            self.diction[nums[i]].append(i)
            
    def pick(self, target: int) -> int:
        return random.choice(self.diction[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        set_version = Counter(nums)
        res = []
        
        for num in nums:
            if (num + 1) in set_version or (num - 1) in set_version:
                continue
            if set_version[num] != 1:
                continue
            res.append(num)
        
        return res
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        diction = {}
        for i in range(len(nums)):
            if nums[i] in diction and (i - diction[nums[i]]) <=k:
                return True
            diction[nums[i]] = i
        return False
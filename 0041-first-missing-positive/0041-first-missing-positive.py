class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            while nums[i] - 1 != i and nums[i] <= N and nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(N):
            if nums[i] - 1 != i:
                return i + 1

        return N + 1

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        res = [-1] * len(nums)

        if 2 * k + 1 > len(nums):
            return res

        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, len(nums) - k):
            l, r = i - k, i + k
            subArraySum = prefix[r + 1] - prefix[l]
            t = subArraySum // (2 * k + 1)
            res[i] = t

        return res
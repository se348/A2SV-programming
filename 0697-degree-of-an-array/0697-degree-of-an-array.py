class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        
        for i in range(len(nums)):
            curr =nums[i]
            if curr not in left: left[curr] = i
            right[curr] = i
            count[curr] = count.get(curr, 0) + 1

        res = len(nums)
        degree = max(count.values())
        for a in count:
            if count[a] == degree:
                res = min(res, right[a] - left[a] + 1)

        return res

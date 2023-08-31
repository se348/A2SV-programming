class Solution:
    def findLargestPartition(self, number, prev) -> tuple:
        a = ceil(number / prev)
        return a - 1, number // a

    def minimumReplacement(self, nums: List[int]) -> int:
#        [12, 9, 7, 6, 17, 19, 21]

        n = len(nums)
        prev_heighest = nums[n - 1]
        res = 0
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= prev_heighest:
                prev_heighest = nums[i]
                continue
            curr_count, curr_heighest = self.findLargestPartition(nums[i], prev_heighest)
            prev_heighest = curr_heighest
            res += curr_count
        return res
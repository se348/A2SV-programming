class Solution:
    def targetIndices(self, nums: list, target: int) -> list:
        nums.sort()
        output =[]
        for i in range(len(nums)):
            if nums[i]== target:
                output.append(i)
        return output

s=Solution()
d =s.targetIndices([1,2,5,2,3],5)
print(d)
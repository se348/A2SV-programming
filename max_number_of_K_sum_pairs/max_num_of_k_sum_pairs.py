class Solution:
    def maxOperations(self, nums: list, k: int) -> int:
        nums.sort()
        counter=0
        i=0
        j=len(nums)-1
        while i< len(nums) and j>i:
            if nums[i] + nums[j] ==k:
                i+=1
                j-=1
                counter +=1
            elif nums[i] + nums[j] <k:
                i+=1
            else:
                j-=1
        return counter
s= Solution().maxOperations([3,1,3,4,3], 6)
print(s)
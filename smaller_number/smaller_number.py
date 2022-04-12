class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        new_list =[]
        for i in range(len(nums)):
            counter =0
            for j in range(len(nums)):
                if i != j:
                    if nums[i]> nums[j]:
                        counter +=1
            new_list.append(counter)
        return new_list

s = Solution()
print(s.smallerNumbersThanCurrent([7,7,7,7]))
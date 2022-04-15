class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        i= 0
        counter=0
        while i< len(nums)-1:
            first_num =nums[i]
            j =i+1
            while j> i and j< len(nums):
                if nums[i] ==nums[j]:
                    counter +=1
                j+=1
            i+=1
        return counter

s =Solution()
a =s.numIdenticalPairs([1,1,1,1])
print(a)
        
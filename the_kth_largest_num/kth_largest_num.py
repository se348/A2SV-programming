class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        i =0 
        while i< len(nums):
            nums[i] = (int)(nums[i])
            i+=1
        nums.sort()
        return f"{nums[len(nums) -k]}"


s =Solution()
nums=["0", "0"]
d =s.kthLargestNumber(nums, 2)
print(d)
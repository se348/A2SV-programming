class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        i =0
        mid =len(nums)//2
        if len(nums) ==3:
            a= nums[0]
            nums[0] = nums[1]
            nums[1] =a

        while i< len(nums)//2:
            if (i%2==1):
                print(i)
                a =nums[i]
                nums[i] =nums[-i -1]
                nums[-i-1] = a
            i+=1
        print(nums)
        if(nums[mid] == (nums[mid-1] +nums[mid+1])/2):
            mid = nums.pop(mid)
            nums.append(mid)
        return nums   
s= Solution()
d= s.rearrangeArray([1,2,3,4,5])
print(d)    
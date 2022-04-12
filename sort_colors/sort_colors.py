class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count =0
        one_count =0
        two_count=0
        for i in nums:
            if i ==0:
                zero_count +=1
            elif i==1:
                one_count +=1
            else:
                two_count +=1
        for i in range(zero_count):
            nums[i] = 0
        for j in range(one_count):
            nums[zero_count +j] = 1
        for k in range(two_count):
            nums[zero_count+one_count +k] =2

s =Solution()
num =[2,0,1]
s.sortColors(num)
print(num)
class Solution:
    def minPairSum(self, nums: list) -> int:
        nums.sort()
        i=0
        a =(int)(len(nums)/2)
        sum_max =[0] * a
        while i< len(nums)/2:
            first_num =nums[i]
            last_num= nums[-(i+1)]
            sum_max[i] = first_num +last_num
            i+=1
        return max(sum_max)
s= Solution()
d =s.minPairSum([3,5,4,2,4,6])
print(d)
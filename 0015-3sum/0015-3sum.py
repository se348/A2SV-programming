class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= {}
        for i in range(len(nums)):
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            while left_ptr < right_ptr:
                curr_total = nums[i] + nums[left_ptr] + nums[right_ptr]
                if curr_total == 0:
                    res[(nums[i], nums[left_ptr],nums[right_ptr])] =1
                    left_ptr+=1
                elif curr_total > 0:
                    right_ptr-=1
                else:
                    left_ptr+=1
        managed = []
        for i,j,k in res:
            managed.append([i,j,k])
        return managed
                                
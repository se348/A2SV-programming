class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff =  math.inf
        nums.sort()
        result = 0
        for i in range(len(nums)):
            left_ptr = i + 1
            right_ptr = len(nums) - 1
            while left_ptr < right_ptr:
                
                curr_total= nums[i] + nums[left_ptr] + nums[right_ptr]
                
                if curr_total==target:
                    result = curr_total
                    break
                elif curr_total< target:
                    if target -curr_total< diff:
                        diff = abs(target - curr_total)
                        result = curr_total
                    left_ptr +=1
                else:
                    if curr_total -target< diff:
                        diff = abs(curr_total - target)
                        result = curr_total
                    right_ptr -=1
        return result
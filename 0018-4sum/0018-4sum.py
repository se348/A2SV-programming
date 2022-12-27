class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res={}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left_ptr = j + 1
                right_ptr = len(nums) - 1
                while left_ptr < right_ptr:
                    curr_total = nums[i] + nums[j] + nums[left_ptr] + nums[right_ptr]
                    if curr_total == target:
                        res[(nums[i] , nums[j] , nums[left_ptr] , nums[right_ptr])] = 1
                        left_ptr += 1
                    elif curr_total< target:
                        left_ptr += 1
                    else: 
                        right_ptr -= 1
        
        ans = []
        for i,j,k,l in res:
            ans.append([i,j,k,l])
        return ans
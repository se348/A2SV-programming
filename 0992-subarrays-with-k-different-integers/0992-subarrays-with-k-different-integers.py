class Solution:
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count_less_than_m(curr_k):
            left = 0
            counter = defaultdict(int)
            res = 0
            
            for right in range(len(nums)):
                counter[nums[right]] += 1
                
                while len(counter) > curr_k:
                    counter[nums[left]] -= 1
                    
                    if counter[nums[left]] == 0:
                        counter.pop(nums[left])
                    
                    left += 1
                res += (right - left + 1)
            return res
        
        
        
        a = count_less_than_m(k)
        b = count_less_than_m(k - 1)
        return a - b
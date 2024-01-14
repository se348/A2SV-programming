class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        count = len(set(nums))
        window_count = defaultdict(int)
        left = 0
        res = 0
        
        for right in range(len(nums)):
            window_count[nums[right]] += 1
            
            prev_left= left
            
            while len(window_count) == count:
                
                window_count[nums[left]] -= 1
                
                if window_count[nums[left]] == 0:
                    window_count.pop(nums[left])
                left += 1
                
            if prev_left != left:
                res += (left - prev_left) * (len(nums) - right )
        
        return res
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        timestwos = []
        plusones = []
        
        
        for num in nums:
            
            curr_times_two = 0
            curr_plus_one = 0
            
            while num:
                if num & 1:
                    num -= 1
                    curr_plus_one += 1
                else:
                    num //= 2
                    curr_times_two += 1
                    
            timestwos.append(curr_times_two)
            plusones.append(curr_plus_one)
        
        return max(timestwos) + sum(plusones)
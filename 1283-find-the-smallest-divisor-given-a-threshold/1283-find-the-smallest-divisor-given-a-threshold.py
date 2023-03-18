class Solution:
    def find_sum(self, nums:List[int], divisor:int):
        total =0
        for n in nums:
            total += ceil(n/divisor)
        return total
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = sum(nums) 
        
        tot = right
        res = 0
        
        while left <= right:
            mid = (left + right) //2
            
            curr = self.find_sum(nums, mid)
            
            if curr > threshold:
                left = mid + 1
                
            else:
                res = mid
                right = mid -1
                
        return res
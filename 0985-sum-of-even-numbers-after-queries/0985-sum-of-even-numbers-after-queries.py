class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        res= []
        for num in nums:
            
            if num % 2 == 0:
                total += num
        
        for val, index in queries:
            curr = nums[index] + val
            
            if nums[index] % 2 == 0 and curr % 2 == 0:
                total += val
                nums[index] = curr
                
            elif nums[index] % 2 == 1 and curr % 2 == 0:
                total += curr
                nums[index] = curr
                
            elif nums[index] % 2 == 0 and curr % 2 == 1:
                total -= nums[index]
                nums[index] = curr
            
            else: 
                total += 0
                nums[index] = curr 
                
            res.append(total)
            
        return res
                
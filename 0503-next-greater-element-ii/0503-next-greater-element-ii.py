class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] 
        next_greater_elem = {}
        
        for i in range(2):
            for ind, num in enumerate(nums):
                while stack and stack[-1][0] < num:
                    prev_num, prev_ind = stack.pop()
                    next_greater_elem[prev_ind] = num
                stack.append((num, ind))
                
        res =[]
        for ind in range(len(nums)):
            res.append(next_greater_elem.get(ind, -1))
            
        return res
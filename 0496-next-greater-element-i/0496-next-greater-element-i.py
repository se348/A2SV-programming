class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterElement = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                nextGreaterElement[stack.pop()] = num
                    
            stack.append(num)
        
        res = []
        
        for num in nums1:
            res.append(nextGreaterElement.get(num, -1))
            
        return res
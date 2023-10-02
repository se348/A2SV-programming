class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for character in s:
            if not stack or stack[-1][0] != character:
                stack.append([character, 1])
                
            elif stack[-1][0] == character:
                stack[-1][1] += 1
                
            if stack[-1][1] == k:
                stack.pop()
            
        result = []
        
        for a, b in stack:
            
            for j in range(b):
                result.append(a)
            
        return "".join(result)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        
        for letter in s:
            
            if letter =="(":
                stack.append("(")
                continue
                
            temp = 0
            
            while stack[-1] != "(":
                temp += stack.pop()
            
            stack.pop()
            
            if temp == 0:
                stack.append(1)
            else:
                stack.append(temp * 2)
        
        return sum(stack)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] == "]":
                curr = []
                
                while stack[-1] != "[":
                    curr.append(stack.pop())
                    
                
                stack.pop()
                
                curr_num= ""
                while stack and stack[-1].isdigit():
                    curr_num += stack.pop()
                
                curr.reverse()
                curr_num = curr_num[::-1]
                stack.extend(curr * int(curr_num))
            
            else:
                stack.append(s[i])
                
        return "".join(stack)
        
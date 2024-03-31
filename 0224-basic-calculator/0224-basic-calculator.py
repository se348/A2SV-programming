class Solution:
    def calculate(self, s: str) -> int:
        open_to_close = {}
        
        def dfs(curr_ind):
            
            curr_computed= 0
            sign =  True
            curr_val = 0
            i = curr_ind
            
            while i < len(s):
                if s[i] == "(":
                    if sign:
                        curr_computed += dfs(i + 1)
                    else:
                        curr_computed -= dfs(i + 1)
                    i = open_to_close[i] + 1
                elif s[i] == ')':
                    if sign:
                        curr_computed += curr_val
                    else:
                        curr_computed -= curr_val
                    curr_val = 0
                    break
                
                elif s[i] == "+":
                    if sign:
                        curr_computed += curr_val
                    else:
                        curr_computed -= curr_val
                    
                    curr_val = 0
                    sign = True
                    i += 1
                elif s[i] == "-":
                    if sign:
                        curr_computed += curr_val
                    else:
                        curr_computed -= curr_val
                        
                    curr_val = 0
                    sign = False
                    i += 1
                elif s[i] == ' ':
                    if sign:
                        curr_computed += curr_val
                    else:
                        curr_computed -= curr_val
                    
                    curr_val = 0
                    i += 1
                else:
                    curr_val *= 10
                    curr_val += int(s[i])
                    i += 1
                    
            if sign:
                curr_computed += curr_val
            else:
                curr_computed -= curr_val
            
            return curr_computed
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            
            elif s[i] == ")":
                open_to_close[stack.pop()] = i

        return dfs(0)
                    
                    
                
                
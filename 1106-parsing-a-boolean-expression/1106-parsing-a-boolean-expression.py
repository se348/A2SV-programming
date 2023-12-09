class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        
        def evaluate(start, end):
            if start == end:
                if expression[start] == "t":
                    return True
            
                return False
            if expression[start] == "!":
                return not evaluate(start + 2, end- 1)
            
            
            curr_scope = 0
            res = True if expression[start] == "&" else False
            prev = start + 2
            
            for i in range(start + 2, end):
                
                if expression[i] == "(":
                    curr_scope += 1
                
                elif expression[i] ==")":
                    curr_scope -= 1

                if curr_scope == 0 and expression[i] == ",":

                    if expression[start] == "&": 
                        res =  res and evaluate(prev, i - 1)
                    
                    else:
                        res = res or evaluate(prev, i - 1)
                    
                    prev = i + 1

            if expression[start] == "&": 
                res =  res and evaluate(prev, end - 1)

            else:
                res = res or evaluate(prev, end - 1)

            return res
        
        return evaluate(0, len(expression) - 1)
                
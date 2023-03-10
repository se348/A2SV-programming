class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                elem1 = stack.pop()
                elem2 = stack.pop()
                
                stack.append(int(elem1) + int (elem2))
            
            elif token == "*":
                elem1 = stack.pop()
                elem2 = stack.pop()
                
                stack.append(int(elem1) * int (elem2))
                
            elif token == "-":
                elem1 = stack.pop()
                elem2 = stack.pop()
                
                stack.append(int(elem2) - int (elem1))
            
            elif token == "/":
                elem1 = stack.pop()
                elem2 = stack.pop()
                
                stack.append(int(int(elem2) / int (elem1)))
                
            else:
                stack.append(token)
        return int(stack[0])
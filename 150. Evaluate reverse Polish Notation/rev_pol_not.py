class Solution:
    def evalRPN(self, tokens: list) -> int:
        i=0
        while True:
            if i== len(tokens):
                break
            if tokens[i]== "+":
                tokens[i-2]= (int)(tokens[i-2]) +(int)(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-1)
                i-=1
            elif tokens[i]== "-":
                tokens[i-2]= (int)(tokens[i-2]) - (int)(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-1)
                i-=1
            elif tokens[i]=='*':
                tokens[i-2]= (int)(tokens[i-2]) * (int)(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-1)
                i-=1
            elif tokens[i]=='/':
                tokens[i-2]= int((int)(tokens[i-2]) / (int)(tokens[i-1]))
                tokens.pop(i-1)
                tokens.pop(i-1)
                i-=1
            else:
                i+=1
        return tokens[0]

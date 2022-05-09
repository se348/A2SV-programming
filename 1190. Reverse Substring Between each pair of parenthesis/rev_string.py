class Solution:
    opening_bracket_stack=[]
    def reverseParentheses(self, s: str) -> str:
        s= list(s)
        i= 0
        while True:
            if i >= len(s):
                break
            if s[i]=="(":
                self.opening_bracket_stack.append(i)
                i+=1
            elif s[i]==")":
                opening =self.opening_bracket_stack.pop()
                s[opening+1: i] = self.reverser(s[opening+1: i]) 
                s.pop(i)
                s.pop(opening)
                i-=1
            else:
                i+=1
        answer ="".join(s)
        return answer

    def reverser(self, part_of_arr):
        return part_of_arr[::-1]
        

s= Solution()
d =s.reverseParentheses("(ed(et(oc))el)") 
print(d)               
        
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:  
        monotonic_stack = []
        if k == len(num):
            return "0"
        for i, j in enumerate(num):
            while (monotonic_stack and k>0 and int(monotonic_stack[-1]) > int(j)):
                monotonic_stack.pop()
                k-=1
            monotonic_stack.append(j)
        while(k>0):
            monotonic_stack.pop()
            k-=1
        monotonic_stack = "".join(monotonic_stack)    
        return str(int(monotonic_stack))
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, n in enumerate(s):
            if not stack or stack[-1][0]!=n:
                stack.append((n,1))
            elif stack and stack[-1][0]==n:
                stack.append((n, stack[-1][-1] + 1))
                if stack and stack[-1][-1] == k:
                    for n in range(k):
                        stack.pop()
        ans= ""
        for n in stack:
            ans+= n[0]
        return ans
            
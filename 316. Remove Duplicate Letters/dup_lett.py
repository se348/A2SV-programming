class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        greatest_index= {}
        for ind, char in enumerate(s):
            greatest_index[char]=ind
        stack=[]
        visited=set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1][-1]>s[i] and greatest_index[stack[-1][-1]]>i:
                visited.remove(stack[-1][-1])
                stack.pop()
            visited.add(s[i])
            stack.append((i,s[i]))
        ans=""
        for i in stack:
            ans+=i[1]
        return ans
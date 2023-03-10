class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        seen = set()
        stack = []
        visited = defaultdict(int)
        for char in s:
            if char in seen:
                visited[char] += 1
            elif not stack or char > stack[-1]:
                visited[char] += 1
                stack.append(char)
                seen.add(char)
            else:
                while stack and char < stack[-1] and visited[stack[-1]] != count[stack[-1]]:
                    seen.remove(stack.pop())
                    
                stack.append(char)
                visited[char] += 1
                seen.add(char)
                
        return "".join(stack)
        
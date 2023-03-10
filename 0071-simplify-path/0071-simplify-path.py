class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        new_path = path.split("/")
        
        for directory in new_path:
            if directory == '.':
                continue
            elif directory == "..":
                while stack and stack[-1] == "":
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        
        res = []
        
        for elem in stack:
            if elem != "":
                res.append("/" + elem)
        
        if not res:
            return "/"
        return "".join(res)
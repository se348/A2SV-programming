class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res= []
        def dfs(idx, curr_traversed):
            if idx >= len(s) and len(curr_traversed) ==4:
                res.append(".".join(curr_traversed))

            if idx < len(s) and len(str(int(s[idx]))) ==len(s[idx]): 
                new = curr_traversed.copy()
                new.append(str(s[idx]))
                dfs(idx+1,new)
            if idx + 1 < len(s) and len(str(int(s[idx: idx+2]))) == len(s[idx:idx+2]):
                new = curr_traversed.copy()
                new.append(str(s[idx: idx + 2]))
                dfs(idx+2,new)
            if idx + 2 < len(s) and len(str(int(s[idx: idx+3]))) == len(s[idx:idx+3]) and int(s[idx:idx+3])<256:
                new = curr_traversed.copy()
                new.append(str(s[idx: idx + 3]))
                dfs(idx+3,new)
        dfs(0,[])
        return res
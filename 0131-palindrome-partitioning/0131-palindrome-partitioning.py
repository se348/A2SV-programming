class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res  = []
        curr = []
        
        def check_is_palindrome(s, l, r):
            while l <= r :
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def dfs(ind):
            
            if ind == len(s):
                res.append(curr[:])
                return 
            
            for i in range(ind + 1, len(s) + 1):
                if check_is_palindrome(s, ind, i - 1):
                    curr.append(s[ind: i])
                    dfs(i)
                    curr.pop()
        
        dfs(0)
        return res
                    
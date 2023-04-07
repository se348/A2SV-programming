class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arrs = [0 ] * k
        if len(cookies) == k:
            return max(cookies)
        def dfs(arrs, ind):
            if ind == len(cookies):
                maxim = max(arrs)
                return maxim
            
            minim = math.inf
            for i in range(k):
                arrs[i] += cookies[ind]
                minim = min(dfs(arrs, ind + 1), minim)
                arrs[i] -= cookies[ind]
            
            return minim
        return dfs(arrs, 0)
                
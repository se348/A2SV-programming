class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        count = 0
        
        def dfs(traversed= []):
            nonlocal count
            
            if len(traversed) == n:
                count += 1
            
            if count == k:
                return traversed[:]
            
            max_attained = math.factorial(n - len(traversed))
            if  max_attained + count < k:
                count  += max_attained
                return
            
            
            for i in range(1, n + 1):
                if str(i) not in traversed:
                    
                    traversed.append(str(i))
                    temp = dfs(traversed)
                    
                    if temp: return temp
                    
                    traversed.pop()
                    
        return "".join(dfs())
                    
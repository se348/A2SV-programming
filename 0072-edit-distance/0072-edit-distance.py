class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        @cache
        def dfs(indx1, indx2):
            
            if indx1 >= len(word1):
                return len(word2) - indx2
            
            if indx2 >= len(word2):
                return len(word1) - indx1
            
            if word1[indx1] == word2[indx2]:
                return dfs(indx1 + 1, indx2 + 1)
            
            opt1 = dfs(indx1 + 1, indx2 + 1) + 1
            opt2 = dfs(indx1 + 1, indx2) + 1
            opt3 = dfs(indx1, indx2 + 1) + 1
            
            return min(opt1, opt2, opt3)
        
        return dfs(0, 0)
        
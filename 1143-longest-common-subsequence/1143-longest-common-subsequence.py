class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        prev = [0 for _ in range(len(text2) + 1)] 
        new = [0 for _ in range(len(text2) + 1)]
        
        for i in range(len(text1) -1, -1, -1):
            prev = new
            new = [0 for _ in range(len(text2) + 1)]
            
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    new[j] = 1 + prev[j + 1]
                else:                    
                    new[j] = max(prev[j], new[j + 1])
            
        return new[0]
                
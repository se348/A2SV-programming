class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmask_arr = []
        
        for word in words:
            bit_rep = 0
            
            for char in word:
                ind =  ord(char) - ord('a')
                bit_rep = bit_rep | (1 << ind)
                
            bitmask_arr.append(bit_rep)
            
        
        n = len(words)
        res = 0
        
        for i in range(n- 1):
            for j in range(i+1, n):
                if not (bitmask_arr[i] & bitmask_arr[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
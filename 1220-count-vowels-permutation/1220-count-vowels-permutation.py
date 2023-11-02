class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rule = { "a" : ['e'], "e": ["a", "i"], "i":["a", "e", "o", "u"], "o": ["i", "u"], "u": ["a"]}
        
        
        @cache
        def dp(remaining, curr_letter):
            if remaining == 1:
                return 1
            
            res = 0
            
            for neighbor in rule[curr_letter]:
                res +=  dp(remaining - 1, neighbor)
            
            modulo = ((10 ** 9) + 7)
            return res % modulo
        
        
        res = 0
        chars = ["a", "e", "i", "o", "u"]
        
        for char in chars:
            res += dp(n, char)
        
        return (res % (10 ** 9 + 7))
        
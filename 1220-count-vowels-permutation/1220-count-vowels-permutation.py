class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rule = { "a" : ['e'], "e": ["a", "i"], "i":["a", "e", "o", "u"], "o": ["i", "u"], "u": ["a"]}
        
        chars = ["a", "e", "i", "o", "u"]
        diction = {char: 1 for char in chars}
        for i in range(n -1):
            new_diction = defaultdict(int)
            
            for char in chars:
                for neighbor in rule[char]:
                    new_diction[char] = (new_diction[char] + diction[neighbor]) % (10 ** 9 + 7)
            diction = new_diction
        
        total = 0
        
        for i in diction:
            total += diction[i]
        
        return (total % (10 ** 9 + 7))
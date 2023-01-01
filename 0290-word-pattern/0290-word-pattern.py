class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        word_list = s.split()
        matcher = {}
        another_matcher = {}
        if len(word_list) != len(pattern):
            return False
        for index, char in enumerate(pattern):
            
            if char in matcher and word_list[index] != matcher[char]:
                return False
            elif char in matcher and word_list[index] != matcher[char] and another_matcher[word_list[index]] != char:
                return False
            elif word_list[index] in another_matcher and another_matcher[word_list[index]] != char:
                return False
            elif char not in matcher:
                matcher[char] = word_list[index]
                another_matcher[word_list[index]] = char
        return True
                
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dictionary={}
        word_dictionary={}
        lists = s.split()
        if len(pattern)!= len(lists):
            return False
        for i,n in enumerate(lists):
            if pattern[i] in pattern_dictionary:
                if pattern_dictionary[pattern[i]] != n:
                    return False
            if n in word_dictionary:
                if word_dictionary[n] != pattern[i]:
                    return False
            else:
                pattern_dictionary[pattern[i]] =n
                word_dictionary[n] =pattern[i]
        return True
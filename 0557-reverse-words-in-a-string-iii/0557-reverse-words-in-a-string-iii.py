class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split(" ")
        for index, word in enumerate(splitted):
            splitted[index] = word[::-1]
        return " ".join(splitted)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=""
        for i, word in enumerate(strs):
            if i==0:
                curr=word
            else:
                new= curr
                curr=""
                for j in range(min(len(new), len(word))):
                    if new[j]== word[j]:
                        curr+= new[j]
                    else: break
        return curr

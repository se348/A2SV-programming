class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            isLexicographical = True
            curr= ""
            for j in range(len(strs)):
                if j==0:
                    curr =strs[j][i]
                else:
                    if curr <= strs[j][i]:
                        curr = strs[j][i]
                        continue
                    else: 
                        isLexicographical = False
                        break
            if not isLexicographical:
                count += 1
        
        return count
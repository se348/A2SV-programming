from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = sorted("qwertyuiop")
        row_2 =sorted("asdfghjkl")
        row_3 = sorted("zxcvbnm")
        
        
        ans=[]
        for n in words:
            condition=1
            appearing =None
            word = n.lower()
            for i , letter in enumerate(word):
                if i==0:
                    if letter in row_1:
                        appearing = row_1
                    elif letter in row_2:
                        appearing = row_2
                    else:
                        appearing = row_3
                    continue
                else:
                    if letter in appearing:
                        continue
                    else:
                        condition =0
                        break
            if condition ==1:
                ans.append(n)
                        
        return ans
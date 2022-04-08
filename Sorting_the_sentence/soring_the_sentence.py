class Solution:
    def sortSentence(self, s: str) -> str:
        l =s.split(" ")
        new_l =[""] * (len(l))
        for i in l:
            a= (int)(i[-1])
            new_l[a- 1] = i[:-1]
        return " ".join(new_l)


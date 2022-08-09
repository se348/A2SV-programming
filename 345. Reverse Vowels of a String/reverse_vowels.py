class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        l=0
        r= len(s)-1
        llist= []
        for n in s:
            llist.append(n)
        while l<=r:
            if llist[l] in vowels and llist[r] in vowels:
                llist[l] ,llist[r] = llist[r], llist[l]
                l+=1
                r-=1
            elif llist[l] in vowels:
                r-=1
            elif llist[r] in vowels:
                l+=1
            else:
                l+=1
                r-=1
        return "".join(llist)


s= Solution()
a =s.reverseVowels("aA")
print(a)
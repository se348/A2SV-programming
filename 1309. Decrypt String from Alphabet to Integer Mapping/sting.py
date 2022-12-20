class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = s.split("#")
        res=["" for _ in range(len(ans))]
        print(ans)
        for j in range(len(ans)-1):
            char= ans[j]
            curr=""
            i=0
            while i<len(char)-2:
                curr+= chr(int(char[i]) + ord("a")-1)
                i+=1
            curr+= chr(int(char[i:i+2])+ ord("a")-1)
            res[j]=curr
        i=0
        curr=""
        while i<len(ans[-1]):
            curr+= chr(int(ans[-1][i]) + ord("a")-1)
            i+=1
        res[-1]= curr
        return "".join(res)
            
        
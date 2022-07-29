class Solution:
    def findComplement(self, num: int) -> int:
        res =self.changeToBin(num)
        a =self.complementStr(res)
        return self.convertToInt(a)
    def changeToBin(self,num):
        stringa =""
        for i in range(31, -1,-1):
            if num >= 2** i:
                stringa+="1"
                num-= 2**i
            else:
                stringa+="0"
        return str(int(stringa))
    def convertToInt(self, bin):
        bin =bin[::-1]
        num= 0
        for i, e in enumerate(bin):
            if e=="1":
                num += 2**i
        return num
    def complementStr(self, resulta):
        res =""
        for n in resulta:
            if n=="1":
                res+="0"
            else:
                res+="1"
        return res
s =Solution()
a = s.findComplement(1)
print(a)
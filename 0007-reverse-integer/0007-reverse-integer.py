class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x= str(x)
            x= x[1:]
            l="-"
            for i in range(len(x)):
                l += f"{(x[-(i+1)])}"
            l =(int)(l)
            if l>=2147483647 or l<-2147483648:
                return 0
            return l
        else:
            x= str(x)
            l=""
            for i in range(len(x)):
                l += f"{x[-(i+1)]}"
            l =(int)(l)
            if l>=2147483647 or l<-2147483648:
                return 0
            return l
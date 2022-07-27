class Solution:
    def addBinary(self, a: str, b: str) -> str:
        current =0
        a =a[::-1]
        b= b[::-1]
        ans=[]
        i= 0
        while i< min(len(a), len(b)):
            if int(a[i]) + int(b[i]) +current <=1:
                ans.append(str(int(a[i]) + int(b[i]) +current))
                current =0
            elif int(a[i]) + int(b[i]) +current ==2:
                current=1
                ans.append(str(0))
            else:
                current=1
                ans.append(str(1))
            i+=1
            
        while i< len(a):
            if current ==1:
                if int(a[i]) + current <=1:
                    ans.append(str(int(a[i]) +current))
                    current =0
                else:
                    current=1
                    ans.append(str(0))
            else:
                ans.append(a[i])
            i+=1
        while i< len(b):
            if current ==1:
                if int(b[i]) + current <=1:
                    ans.append(str(int(b[i]) +current))
                    current =0
                else:
                    current=1
                    ans.append(str(0))
            else:
                ans.append(str(b[i]))
            i+=1
        if current==1:
            ans.append(str(1))
        return "".join(ans)[::-1]
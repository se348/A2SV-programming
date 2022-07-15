class Solution:
    def decodeString(self, s: str) -> str:
        stck =[]
        i =0
        while i< len(s):
            print(stck)
            if s[i].isdigit():
                stck.append(s[i])
                i+=1
            elif s[i]=="[":
                stck.append(s[i])
                i+=1
            elif s[i]=="]":
                new_string=""
                while stck[-1] != "[":
                    new_string= stck.pop() + new_string
                stck.pop()
                count =""
                while stck and stck[-1].isdigit():
                    count = stck.pop() + count
                print("count"+ count)
                new_string *= int(count)
                stck.append(new_string)
                i+=1
            else:
                stck.append(s[i])
                i+=1
        return "".join(stck)

s= Solution()
a =s.decodeString("3[a2[c]]")
print(a)
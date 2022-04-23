class Solution:
    def minSetSize(self, arr: list) -> int:
        unique_elems={}
        for elem in arr:
            if len(unique_elems)==0 or elem not in unique_elems:
                unique_elems[elem] =1
            else:
                unique_elems[elem] +=1
        a =unique_elems.values()
        a=list(a)
        a.sort()
        b=0
        d= 0
        while d< len(arr)//2:

            d+=a[-1]
            a.pop()
            b+=1
        return b

s= Solution()
b= s.minSetSize([1,9])
print(b)
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def lessThanNum(num):
            tot= 0
            for i in range(1,m+1):
                tot += min(num//i, n)
            return tot
        l =1
        r= m *n
        ans =-1
        while l<=r:
            mid=(l+r)//2
            count= lessThanNum(mid)
            if count >=k:
                ans =mid
                r =mid-1
            else:
                l= mid+1
        return ans
            
s = Solution()
a =s.findKthNumber(2,3,4)
print(a)
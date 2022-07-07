class Solution:
    
    def findKthBit(self, n, k):
        return self.helper(n, k)[k-1] 
    def helper(self, n: int, k: int) -> str:
        if n==0:
            return "0"
        tempo= self.helper(n-1, k)
        return tempo +"1" + self.invert(tempo)[::-1]
    def invert(self, tempo):
        inverted=""
        for n in tempo:
            inverted += "0" if n=="1" else "1"
        return inverted



s= Solution()
a = s.findKthBit(4,11)
print(a)
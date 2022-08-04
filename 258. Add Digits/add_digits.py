class Solution:
    def addDigits(self, num: int) -> int:
        sum =0
        for n in str(num):
            sum+= int(n)
        if sum>=10:
            return self.addDigits(sum)
        else: return sum
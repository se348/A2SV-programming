class Solution:
    def __init__(self):
        self.belowTwenty = {
            1:" One", 2:" Two", 3:" Three",
            4:" Four",5:" Five",6:" Six",7:" Seven",
            8:" Eight",9:" Nine",10:" Ten",11:" Eleven",
            12:" Twelve",13:" Thirteen",14:" Fourteen",
            15:" Fifteen", 16:" Sixteen", 17:" Seventeen",
            18:" Eighteen", 19:" Nineteen"
        }

        self.tenth = {
            2:" Twenty", 3:" Thirty", 4:" Forty",
            5:" Fifty", 6:" Sixty", 7:" Seventy",
            8:" Eighty", 9:" Ninety"
        }

    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        else: 
            return self.helper(num, 0).strip()
    def helper(self, num, power):
        if num==0:
            return ""
        if num< 1000 and power ==0:
            return self.dealwithLessthanThousand(num)
        if num< 1000 and power==1:
            return self.dealwithLessthanThousand(num) + " Thousand"
        if num< 1000 and power==2:
            return self.dealwithLessthanThousand(num) + " Million"
        if num< 1000 and power==3:
            return self.dealwithLessthanThousand(num) + " Billion"
        return self.helper(num//1000, power +1) + self.helper(num%1000, power)
        
    def dealwithLessthanThousand(self, num):
        if num< 20:
            return self.belowTwenty[num]
        if num< 100:
            if num % 10== 0:
                remainder =""
            else: 
                remainder  = self.belowTwenty[num % 10]
            return self.tenth[num//10] +  remainder
        if num< 1000:
            if num % 100== 0:
                remainder =""
            else: 
                remainder  = self.dealwithLessthanThousand(num%100)
            return self.belowTwenty[num//100] + " Hundred" + remainder
    
s= Solution()
a = s.numberToWords(48298383)
print(a)
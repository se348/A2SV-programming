class Solution:
    def intToRoman(self, num: int) -> str:
        print(num)
        if num==0: return ""
        if num>= 900:
            if num>=1000: 
                if (num-1000)< 1000:
                    return "M"+ self.intToRoman(num%1000)
                else:
                    re= "M"* int(num//1000)
                    return re +self.intToRoman(num%1000)
            else: 
                return "CM" +self.intToRoman(num%900)
        elif num>= 400:
            if num>=500: 
                return "D"+ self.intToRoman(num%500)
            else: 
                return "CD"+ self.intToRoman(num%400)
        elif num>= 90:
            if num>=100: 
                if(num-100)<100:
                    return "C"+self.intToRoman(num%100)
                else:
                    re ="C" * int(num//100)
                    return re+self.intToRoman(num%100)
            else: 
                return "XC" +self.intToRoman(num%90)
        elif num>= 40:
            if num>=50: 
                return "L" +self.intToRoman(num%50)
            else: 
                return "XL"+ self.intToRoman(num%40)
        elif num>= 9:
            if num>=10: 
                if(num-10)< 10:
                    return"X"+ self.intToRoman(num%10)
                else:
                    re ="X"* int(num//10)
                    return re+ self.intToRoman(num%10)
            else: 
                return"IX"+ self.intToRoman(num%9)
        elif num>= 4:
            if num>=5: 
                return"V"+ self.intToRoman(num%5)
            else: 
                return "IV" +self.intToRoman(num%4)
        elif num< 4:
            if num==1: return "I" 
            if num==2: return "II"
            if num==3: return "III"

s= Solution()
a =s.intToRoman(2384)
print(a)
class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        previous=None
        for l in s:
            if previous=="I" and l=="V":
                number+= 3
                previous="V"
            elif previous=="I" and l=="X":
                number+= 8
                previous="X"
            elif previous=="X" and l=="L":
                number+= 30
                previous="L"
            elif previous=="X" and l=="C":
                number+= 80
                previous="C"
            elif previous=="C" and l=="D":
                number+= 300
                previous="D"
            elif previous=="C" and l=="M":
                number+= 800
                previous="M"
            elif l=="M":
                previous ="M"
                number +=1000
            elif l=="D":
                previous ="D"
                number +=500
            elif l=="C":
                previous ="C"
                number +=100
            elif l=="L":
                previous ="L"
                number +=50
            elif l=="X":
                previous ="X"
                number +=10
            elif l=="V":
                previous ="V"
                number +=5
            elif l=="I":
                previous ="I"
                number +=1
        return number
    
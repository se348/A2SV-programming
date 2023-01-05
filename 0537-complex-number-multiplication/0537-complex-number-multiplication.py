class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = num1.split("+")
        real2, imag2 = num2.split("+")
        
        real1 = int(real1)
        real2 = int(real2)
        
        imag1 = int(imag1[:-1])
        imag2 = int(imag2[:-1])
        
        
        first_part = (real1 * real2) - (imag1 * imag2)
        
        second_part = (real1 * imag2) + (real2 * imag1)
        
        return f"{str(first_part)}+{str(second_part)}i"
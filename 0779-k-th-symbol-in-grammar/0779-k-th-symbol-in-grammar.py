class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        # 0110100110010110
        
        if k == 1:
            return 0
        
        power_2 = 1        
        
        while power_2 < k:
            power_2 <<= 1
        
        power_2 >>= 1
        current= k - power_2
        
        res = 1
        while current > 2:
            power_2 >>= 1
            if current < power_2:
                continue
            if current == power_2:
                current //= 2
            else:
                current = current - power_2
            res += 1
        if current == 2:
            res+= 1
        
        return (res & 1)
        
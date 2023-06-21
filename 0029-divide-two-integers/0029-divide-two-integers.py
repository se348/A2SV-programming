class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def solve(dividend, divisor):
            if dividend < divisor:
                return 0

            bitmask = 1
            count = 0

            while dividend - (divisor << bitmask)>=0:
                count += 1
                bitmask += 1

            temp= dividend -(divisor << count)
            return (1 << count) + solve(temp, divisor)
        
        curr_dividend = abs(dividend)
        curr_divisor = abs(divisor)
        
        curr_ans = solve(curr_dividend, curr_divisor)
        
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            if curr_ans >= 2 ** 31:
                return (2 ** 31) -1
            return curr_ans
        
        if curr_ans < -2 ** 31:
            return (-2 ** 31)
        return -curr_ans
        
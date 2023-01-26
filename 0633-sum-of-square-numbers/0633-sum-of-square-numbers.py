class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares= [ ]
        
        for num in range(c + 1):
            if num * num <= c:
                squares.append(num)
            else:
                break
                
        left_ptr = 0
        right_ptr = len(squares) -1
        
        while left_ptr <= right_ptr:
            num1 = squares[left_ptr]
            num2 = squares[right_ptr]
            
            temp = (num1 ** 2) + (num2 ** 2)
            
            if temp < c:
                left_ptr += 1
            
            elif temp > c:
                right_ptr -= 1
                
            else:
                return True
            
        return False
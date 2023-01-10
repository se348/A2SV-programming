class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num % 3 == 0:
            
            dividend = num //3
            return [dividend-1, dividend, dividend+1]
        else:
            return []
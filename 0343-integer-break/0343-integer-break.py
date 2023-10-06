class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def dp(curr_number):
            if curr_number <= 2:
                return 1
            if curr_number == 3:
                return 2
            if curr_number == 4:
                return 4
            
            res = 0
            for num in range(1, curr_number):
                diff = curr_number - num
                
                opt1 = diff * num
                temp1, temp2 = dp(diff) , dp(num)
                
                opt2 = temp1 * temp2
                opt3 = temp1 * num
                opt4 = diff * temp2
                
                res =max(res, opt1, opt2, opt3, opt4)
            
            return res
       
        return dp(n)
    
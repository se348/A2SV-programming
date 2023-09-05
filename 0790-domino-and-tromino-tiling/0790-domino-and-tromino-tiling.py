class Solution:
    def numTilings(self, n: int) -> int:
        
        memo= {}
        
        def dp(curr_top, curr_bottom):
            if curr_top == n- 1 and curr_bottom == n -1:
                return 1
            if curr_top >= n or curr_bottom >= n:
                return 0
            if (curr_top, curr_bottom) in memo:
                return memo[(curr_top, curr_bottom)]
            if curr_top == curr_bottom:
                a = dp(curr_top + 1, curr_bottom + 1)
                b = dp(curr_top + 2, curr_bottom + 1)
                c = dp(curr_top + 1, curr_bottom + 2)
                d = dp(curr_top + 2, curr_bottom + 2)
                memo[(curr_top, curr_bottom)] = a + b + c + d
                return a + b + c + d
            
            elif curr_top == curr_bottom + 1:
                a = dp(curr_top, curr_bottom + 2)
                b = dp(curr_top + 1, curr_bottom + 2)
                memo[(curr_top, curr_bottom)] = a + b 
                return a + b
            elif curr_top + 1 == curr_bottom:
                a = dp(curr_top + 2, curr_bottom)
                b = dp(curr_top + 2, curr_bottom + 1)
                memo[(curr_top, curr_bottom)] = a + b
                return a + b
            elif curr_top > curr_bottom + 1:
                temp = dp(curr_top, curr_bottom + 2)
                memo[(curr_top, curr_bottom)] = temp
                return temp
            elif curr_bottom > curr_top + 1:
                temp =  dp(curr_top + 2, curr_bottom)
                memo[(curr_top, curr_bottom)] = temp
                return temp
        return( dp(-1, -1) % ((10** 9) + 7))
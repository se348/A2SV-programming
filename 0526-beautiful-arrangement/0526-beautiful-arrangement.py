class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        
        def dfs(curr_number, curr_index, flag):
            if not ((curr_number % curr_index) == 0 or (curr_index % curr_number) == 0):
                return 
            
            if (2 ** n) - 1 == flag:
                nonlocal res
                res += 1
                
            for i in range(1, n + 1):
                next_number = (2 ** (i - 1))
                if next_number & flag:
                    continue
                
                next_flag = next_number | flag
                
                dfs(i, curr_index +1, next_flag)
        
        
        for i in range(1, n + 1):
            flag  = (2 ** (i - 1))
            dfs(i, 1, flag)
        
        return res
                
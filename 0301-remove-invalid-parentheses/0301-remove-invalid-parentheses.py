class Solution:
    def count_removal(self, s: str):
        left_count = 0
        right_count = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                left_count += 1
                
            elif s[i] == ")":
                if left_count == 0:
                    right_count += 1
                else:
                    left_count -= 1
    
        return left_count, right_count
    def check(self, s: str):
        left_count = 0
        
        for i in range(len(s)):
            
            if s[i] == "(":
                left_count += 1
                
            elif s[i] == ")":
                if left_count == 0:
                    return False
                left_count -= 1
    
        return left_count == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        lf_rm, rt_rm = self.count_removal(s)
        result = set()
        
        def backtrack(curr_s, ind, cur_left_removed, curr_right_removed):
            nonlocal lf_rm, rt_rm
            
            if ind == len(s):
                if cur_left_removed == lf_rm and curr_right_removed == rt_rm and self.check(curr_s):
                    result.add(curr_s)
                return
            
            if s[ind].isalpha():
                return backtrack(curr_s + s[ind], ind + 1, cur_left_removed, curr_right_removed)
            
            if s[ind] == "(" and cur_left_removed != lf_rm:
                backtrack(curr_s, ind + 1, cur_left_removed + 1, curr_right_removed)
            
            elif s[ind] == ")" and curr_right_removed != rt_rm:
                backtrack(curr_s, ind + 1, cur_left_removed, curr_right_removed + 1)
                
            backtrack(curr_s + s[ind], ind + 1, cur_left_removed, curr_right_removed)
        
        backtrack("", 0, 0, 0)
        
        return result
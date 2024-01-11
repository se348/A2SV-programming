# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        res = 0
        
        def dfs(curr_node):
            nonlocal res
            
            if not curr_node:
                return [0, False]
            
            left_dist, left_found = dfs(curr_node.left)
            right_dist, right_found = dfs(curr_node.right)
            

            if curr_node.val == start:
                res = max(res, left_dist, right_dist)
                return [1, True]
            
            if left_found:
                res = max(res, abs(left_dist +  right_dist))
                return [1 + left_dist, left_found]
            
            if right_found:
                res = max(res, abs(left_dist +  right_dist))
                return [1 + right_dist, right_found]
            
            return [1 + max(right_dist, left_dist), False]
        
        dfs(root)
        return res
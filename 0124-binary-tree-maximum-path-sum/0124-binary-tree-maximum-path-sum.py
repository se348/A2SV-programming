# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -math.inf
        
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            
            temp = 0
            curr_res = curr.val
            
            left_res = max(dfs(curr.left), 0)
            right_res= max(dfs(curr.right), 0)
          
            res= max(right_res + left_res + curr.val, res)
            return max(left_res, right_res) + curr.val
        
        res = max(dfs(root), res)
        return res
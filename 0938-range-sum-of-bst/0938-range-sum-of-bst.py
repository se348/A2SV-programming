# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(curr_node):
            if not curr_node:
                return 0
            
            temp = 0
            
            if low <= curr_node.val <=  high:
                temp += curr_node.val
                
            temp += dfs(curr_node.left)
            temp += dfs(curr_node.right)
            
            return temp
            
        return dfs(root)
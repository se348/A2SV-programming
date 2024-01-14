# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr_node):
            
            if not curr_node:
                return 0
            
            l = dfs(curr_node.left)
            r = dfs(curr_node.right)
            
            return 1 + max(l, r)
        
        
        def recurse(curr_node, curr_depth, max_depth):
            if not curr_node:
                return 0
            
            if curr_depth == max_depth:
                return curr_node.val
            
            a = recurse(curr_node.left, curr_depth + 1, max_depth)
            b = recurse(curr_node.right, curr_depth + 1, max_depth)
            
            return a + b
        
        max_depth = dfs(root)
        return recurse(root, 1, max_depth)
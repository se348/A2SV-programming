# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(curr):
            if not curr:
                return ""
            
            currString = f"{curr.val}"
            
            if curr.left or curr.right:
                tempLeft = dfs(curr.left)
                tempRight = dfs(curr.right)
                
                if curr.right:
                    currString = f"{currString}({tempLeft})({tempRight})"
                else:
                    currString = f"{currString}({tempLeft})"
            return currString
        
        return dfs(root)
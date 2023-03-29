# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
        if not root:
            return True
        
        a = self.isValidBST(root.left, left, root.val)
        b = self.isValidBST(root.right, root.val, right)
        c= False
        if left < root.val < right:
            c = True
        return a and b and c
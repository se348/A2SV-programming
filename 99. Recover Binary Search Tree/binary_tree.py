# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    swapper1 =None
    swapper2=None
    swapper3=None
    prev=None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            if self.prev and self.prev.val> root.val:
                if self.swapper1 is None:
                    self.swapper1 =self.prev
                    self.swapper2= root
                else:
                    self.swapper3 =root
            self.prev=root
            dfs(root.right)
        dfs(root)
        if self.swapper3:
            self.swapper1.val, self.swapper3.val = self.swapper3.val, self.swapper1.val
        else:
            self.swapper1.val, self.swapper2.val = self.swapper2.val, self.swapper1.val
        
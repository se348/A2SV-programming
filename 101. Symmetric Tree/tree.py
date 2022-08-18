# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        llist=[]
        def inorder_traversal(root,level):
            if not root:
                return
            inorder_traversal(root.left,level+1)
            llist.append((root.val,level))
            inorder_traversal(root.right,level+1)
        inorder_traversal(root,0)
        print(llist)
        return llist ==llist[::-1]
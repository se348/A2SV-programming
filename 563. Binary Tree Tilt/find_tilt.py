# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    tilt=0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root:
            self.helper(root)
        return self.tilt
    def helper(self, curr):
        if not curr:
            return 0
        curr_val= curr.val
        a = self.helper(curr.left)
        b= self.helper(curr.right)
        self.tilt += abs(a-b)
        return curr_val+ a+ b
        